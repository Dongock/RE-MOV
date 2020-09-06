from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Review, Comment, Recomment, ShortReview, Report
from .forms import ReviewForm, CommentForm, RecommentForm, ShortReviewForm, ReportForm
from movies.models import Movie
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/review_list.html', context)

@login_required
def create(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()

            return redirect('community:detail', review.pk)

    else:
        form = ReviewForm()
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'community/form.html', context)

@login_required
def shortcreate(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ShortReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            return redirect('community:index')
    else:
        form = ShortReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'community/shortform.html', context)


def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.hits += 1 
    review.save()
    comment_form = CommentForm()
    recomment_form = RecommentForm()
    report_form = ReportForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'recomment_form': recomment_form,
        'report_form' : report_form,
    }
    return render(request, 'community/review_detail.html', context)

def shortdetail(request, short_pk):
    shortreview = get_object_or_404(ShortReview, short_pk=pk)
    form = ReportForm()
    context = {
        'shortreview':shortreview,
        'form': form,
    }
    return render(request, 'community/shortreview_detail.html', context)

@login_required
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user  == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save(commit=false)
                review.updated_at = datetime.now()
                review.hits -= 1
                review.save()
                return redirect('community:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
        context = {
            'form': form
        }
        return render(request, 'community/form.html', context)
    else:
        messages.warning(request, '해당 페이지에 권한이 없습니다.')
        return redirect('community:detail', review.pk)


@login_required
def shortupdate(request, short_pk):
    shortreview = get_object_or_404(ShortReview, short_pk=pk)
    if request.method == 'POST':
        form = ShortReviewForm(request.POST, instance=shortreview)
        if form.is_valid():
            shortreview = form.save()
            return redirect('community:shortdetail', short_pk)
    else:
        form = ShortReviewForm(instance=shortreivew)
    context = {
        'form': form,
    }
    return render(request, 'community/shortform.html', context)


@require_POST
@login_required
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('community:index')

@require_POST
@login_required
def shortdelete(request, short_pk):
    shortreview = get_object_or_404(ShortReview, short_pk=pk)
    shortreview.delete()
    return redirect('community:index')


@login_required
def comments_create(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment= comment_form.save(commit=False)
            comment.review=review
            comment.user=request.user
            comment.save()
            review.hits -= 1
            review.save()
            return redirect('community:detail',review_pk)


@login_required
def recomments_create(request,review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        recomment_form = RecommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.comment = comment
            recomment.user = request.user
            recomment.save()
            review.hits -= 1
            review.save()
            return redirect('community:detail', review_pk)


@login_required
def comments_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk= comment_pk)
    comment.delete()
    review = get_object_or_404(Review, review_pk)
    review.hits -=1 
    review.save()
    return redirect('community:detail', review_pk)

@login_required
def recomments_delete(request, review_pk, recomment_pk):
    recomment = get_object_or_404(Recomment, pk=recomment_pk)
    recomment.delete()
    review = get_object_or_404(Review, pk=review_pk)
    review.hits -=1
    review.save()
    return redirect('community:detail', review_pk)

@login_required
def report(request):
    if request.user.is_admin:
        reports = Report.objects.all().order_by('-pk')
        reviews = Review.objects.all()
        comments = Comment.objects.all()
        recomments = Recomment.objects.all()
        shortreviews = ShortReview.objects.all()
        context = {
        'reports': reports,
        'reviews': reviews,
        'comments': comments,
        'recomments' : recomments,
        'shortreviews' : shortreviews
        }
        return render(request, 'community/report.html', context)
    else:
        messages.warning(request, '해당 페이지에 권한이 없습니다.')
        return redirect('community:index')

def report_to_content(request, pk):
    pass


def shortreview_list(request):
    short_reviews = ShortReview.objects.all().order_by('-pk')
    context = {
        'short_reviews' : short_reviews
    }
    return render(request, 'community/shortreviewList.html', context)

@login_required
def report_create(request, sort, pk):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        print(form)
        if form.is_valid():
            report= form.save(commit=False)
            report.sort = sort
            report.r_id = pk
            report.reporter = request.user
            report.save()
            messages.success(request, '성공적으로 신고가 접수되었습니다. 관리자가 곧 게시물에 대한 검토를 진행할 예정입니다.')
            return redirect('community:index')
        else:
            messages.warning(request, 'not valid')
            return redirect('community:index')