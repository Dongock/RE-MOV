# :eight_pointed_black_star: 프로젝트 이름 : Re:vanilla



## :busts_in_silhouette: 팀원소개

##### :man: 김정원 : Front 디자인, 메인 페이지, 검색, 계정 설정 및 회원 정보, DB관리

##### :man: 이동옥 : Front 디자인, 커뮤니티 기능, 영화 추천 알고리즘

## :book: 프로젝트 소개​

- 영화는 많은데 볼 영화는 뭐가 있는지 모르겠다면!
- 나와 비슷한 사람들이 찾는 영화를 추천해준다!
- 영화 검색 기능을 통해 찾고 싶은 영화 찾기!
- 한줄 평, 별점, 리뷰, 댓글 기능을 통해 영잘알들과 소통!



## 💻 스택

![Generic badge](https://img.shields.io/badge/platform-Web-brightgreen.svg) ![Generic badge](https://img.shields.io/badge/library-django-blue.svg) ![Generic badge](https://img.shields.io/badge/framework-django-green.svg) ![Generic badge](https://img.shields.io/badge/language-Python-important.svg)



## :game_die: 이용 방법

### IDE

```
VScode
```

### Clone

```
git clone https://github.com/Dongock/RE-MOV.git
```

### Frontend

```
$yarn install
$yarn serve --port 3000
```





## :closed_book: 페이지 별 서비스 설명

#### 1. 메인 페이지

- 검색 기능 (제목이나 출연진을 입력하여 검색)
- 영화를 누르면 모달을 통해 영화 정보 확인 가능
- 회원 가입 시 영화 추천 알고리즘을 반영해 영화 추천

#### 2. 커뮤니티

- 댓글, 대댓글, 좋아요, 리뷰, 한줄 평 작성 가능
- 신고 기능(관리자가 판단)

#### 3. 영화 정보창

- 영화 정보창에서 한줄 평 작성 가능
- 리뷰 작성을 이용하면 리뷰 작성 페이지로 이동

#### 4. 회원가입/로그인

- 회원가입 시 이메일 인증을 통해 회원가입 가능



## :file_folder: 폴더구조

```
📦RE-MOV
 ┣ 📂.git
 ┃ ┣ 📂hooks
 ┃ ┃ ┣ 📜applypatch-msg.sample
 ┃ ┃ ┣ 📜commit-msg.sample
 ┃ ┃ ┣ 📜fsmonitor-watchman.sample
 ┃ ┃ ┣ 📜post-update.sample
 ┃ ┃ ┣ 📜pre-applypatch.sample
 ┃ ┃ ┣ 📜pre-commit.sample
 ┃ ┃ ┣ 📜pre-merge-commit.sample
 ┃ ┃ ┣ 📜pre-push.sample
 ┃ ┃ ┣ 📜pre-rebase.sample
 ┃ ┃ ┣ 📜pre-receive.sample
 ┃ ┃ ┣ 📜prepare-commit-msg.sample
 ┃ ┃ ┗ 📜update.sample
 ┃ ┣ 📂info
 ┃ ┃ ┗ 📜exclude
 ┃ ┣ 📂logs
 ┃ ┃ ┣ 📂refs
 ┃ ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┃ ┗ 📜master
 ┃ ┃ ┃ ┗ 📂remotes
 ┃ ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┃ ┗ 📜master
 ┃ ┃ ┗ 📜HEAD
 ┃ ┣ 📂objects
 ┃ ┃ ┣ 📂02
 ┃ ┃ ┃ ┗ 📜e933fcc3b36021cd2aab4b34a0998fbf9801e8
 ┃ ┃ ┣ 📂0c
 ┃ ┃ ┃ ┗ 📜bee6fae299cd5784024050f1f7cabb42f96ac0
 ┃ ┃ ┣ 📂0d
 ┃ ┃ ┃ ┗ 📜a77ab20f7eccfb5b22b1ac5bd6a3079c7efd5a
 ┃ ┃ ┣ 📂10
 ┃ ┃ ┃ ┗ 📜07b17dae4aaabef4d2d04aa28ecfacccc60209
 ┃ ┃ ┣ 📂12
 ┃ ┃ ┃ ┣ 📜3c0cd569f656c70b6aba39e4f29fc7d015d7d1
 ┃ ┃ ┃ ┗ 📜f180814f13b246cac00cc6acf4bcaebc9c4655
 ┃ ┃ ┣ 📂13
 ┃ ┃ ┃ ┣ 📜072b009fc451e00e6cbc103778e7e7c441a8d9
 ┃ ┃ ┃ ┗ 📜47ace137006cd176aee0c614e4b409589e61f2
 ┃ ┃ ┣ 📂14
 ┃ ┃ ┃ ┗ 📜d2d94de7e810f92df056a8fe4f25f01823ea26
 ┃ ┃ ┣ 📂15
 ┃ ┃ ┃ ┗ 📜7b5976f93a6183b3ab5f039a14d2838bfc1369
 ┃ ┃ ┣ 📂1e
 ┃ ┃ ┃ ┣ 📜37d7c91754d26104651b3b60c1ad2d7bbc9608
 ┃ ┃ ┃ ┗ 📜eff24e29739f395ded02a8bd7c843d250c7f24
 ┃ ┃ ┣ 📂22
 ┃ ┃ ┃ ┣ 📜7c73f09d81b04fa687351c169c06dcc6acc864
 ┃ ┃ ┃ ┗ 📜9a56d8c46d75d9c006af21e9c3933c39f9945b
 ┃ ┃ ┣ 📂25
 ┃ ┃ ┃ ┣ 📜0ef9e3c175f43a6e2f81363da821318ef2a50b
 ┃ ┃ ┃ ┗ 📜b7e3fb2c7e2accef7458e3556093b1fdf0024a
 ┃ ┃ ┣ 📂26
 ┃ ┃ ┃ ┣ 📜233cb6a7c0cefcde9ed42868b3dbb520cf3c81
 ┃ ┃ ┃ ┗ 📜e2a3d4431152b37130763e5eb8153d3c7e52a5
 ┃ ┃ ┣ 📂28
 ┃ ┃ ┃ ┗ 📜5475840d2bdcb5e884d7363cf4450236a76f50
 ┃ ┃ ┣ 📂2a
 ┃ ┃ ┃ ┗ 📜b4c53cb15c2f1d48ba12a0abe4e16983dd0167
 ┃ ┃ ┣ 📂2e
 ┃ ┃ ┃ ┗ 📜56f2cf985e8a9b51cc354f9f761fa052af2f3b
 ┃ ┃ ┣ 📂30
 ┃ ┃ ┃ ┗ 📜3734838ef3f799b2fc2d0d0a94baeb8118547f
 ┃ ┃ ┣ 📂31
 ┃ ┃ ┃ ┣ 📜7e7a763905a846c38b0f566cfc61cf2e5a674b
 ┃ ┃ ┃ ┣ 📜84dbd09a6087c024bb7097b908dca17bf8b7c9
 ┃ ┃ ┃ ┣ 📜d83d12ad9c8a051f5c521af796c4423c47a55f
 ┃ ┃ ┃ ┗ 📜df8ab253b07e554d8ae7ec44d92daa327eb056
 ┃ ┃ ┣ 📂33
 ┃ ┃ ┃ ┗ 📜58d2fb042f5208eaf963c162856bf4e489059f
 ┃ ┃ ┣ 📂35
 ┃ ┃ ┃ ┗ 📜88ab0177ecc2f180de9b4150cd8d473d40fdad
 ┃ ┃ ┣ 📂39
 ┃ ┃ ┃ ┗ 📜bbe2788cbabafd5c80f26a92a4ceb1e062f128
 ┃ ┃ ┣ 📂43
 ┃ ┃ ┃ ┗ 📜bd6a011f4aaf05047bb87cab4bb878aa281b6c
 ┃ ┃ ┣ 📂4a
 ┃ ┃ ┃ ┗ 📜d0548a560dbe82c8af2b8d41f1da94cf58c117
 ┃ ┃ ┣ 📂4b
 ┃ ┃ ┃ ┗ 📜2296a22a9a0e60b3c90498a1331249b2b3866b
 ┃ ┃ ┣ 📂4e
 ┃ ┃ ┃ ┗ 📜96f01fef8b54ee46dcae17a0f4318454b49391
 ┃ ┃ ┣ 📂53
 ┃ ┃ ┃ ┗ 📜97c829060bd98208855075436f8f3215547f66
 ┃ ┃ ┣ 📂56
 ┃ ┃ ┃ ┗ 📜b6be2fdf9957f2d93ea289e90f28a815c33c20
 ┃ ┃ ┣ 📂58
 ┃ ┃ ┃ ┣ 📜a0f544821f07d12c1094196614ee361396fb6d
 ┃ ┃ ┃ ┣ 📜cd5178ab2999615df20966366e80e2ac6e592a
 ┃ ┃ ┃ ┗ 📜fe34c506fb4d0638af52b052a6ea01dbd6ed2d
 ┃ ┃ ┣ 📂5e
 ┃ ┃ ┃ ┗ 📜94575bb5fed54bd70dd754cc89a6160d0303a5
 ┃ ┃ ┣ 📂60
 ┃ ┃ ┃ ┗ 📜1a3f202c7dae0cf8b6d12332977b2e320c7926
 ┃ ┃ ┣ 📂61
 ┃ ┃ ┃ ┗ 📜91999fc75048f6515ede0a987b2dcf843bfe0b
 ┃ ┃ ┣ 📂64
 ┃ ┃ ┃ ┗ 📜6a8932da9cf0b2ecf754d70537bca22f7d7730
 ┃ ┃ ┣ 📂65
 ┃ ┃ ┃ ┗ 📜9eb70f6eb4c033a9a11775acc9f66df57c00f9
 ┃ ┃ ┣ 📂66
 ┃ ┃ ┃ ┗ 📜94e93e0ba31aefb09b58a3003184b7956235c0
 ┃ ┃ ┣ 📂6a
 ┃ ┃ ┃ ┗ 📜23707dc32c517bac9a154eb6a1a24ba95f26eb
 ┃ ┃ ┣ 📂6c
 ┃ ┃ ┃ ┣ 📜51b78fdb1af919e2e9c0f36930e9a9cb8dcc08
 ┃ ┃ ┃ ┗ 📜ae13b97dd4b413cd74aaad40b37e6880862701
 ┃ ┃ ┣ 📂6e
 ┃ ┃ ┃ ┗ 📜bbdb30047a1154a720b657356e279116f59159
 ┃ ┃ ┣ 📂6f
 ┃ ┃ ┃ ┣ 📜a17221a88ab12fa851119f669c4c21efc0a1db
 ┃ ┃ ┃ ┗ 📜c1d83d2ae3bee306eeadf5eba9b1efef84388e
 ┃ ┃ ┣ 📂73
 ┃ ┃ ┃ ┗ 📜083a49d6c7abe2c8a0117b99c0eb19a01fbc43
 ┃ ┃ ┣ 📂74
 ┃ ┃ ┃ ┣ 📜220c9ff0b569658b00504f32297ea47fc06cfc
 ┃ ┃ ┃ ┣ 📜29311b5a1cbd52ff6977751a72e4394d43c0e7
 ┃ ┃ ┃ ┣ 📜3e0d369d3a3b57dc643d8a9730bf7f88996e6c
 ┃ ┃ ┃ ┗ 📜fd0cfb808e7b3601ebf27769b7684d25c9391d
 ┃ ┃ ┣ 📂75
 ┃ ┃ ┃ ┗ 📜d43ca303c0d727b50c12b2910fe283ba0a5186
 ┃ ┃ ┣ 📂76
 ┃ ┃ ┃ ┗ 📜1ba8f9093c6e1a74b68d153b7ae0335ee64a51
 ┃ ┃ ┣ 📂78
 ┃ ┃ ┃ ┗ 📜97a3c895db9a5b368cb9bd9079e3f04b1ac6f6
 ┃ ┃ ┣ 📂7c
 ┃ ┃ ┃ ┗ 📜e503c2dd97ba78597f6ff6e4393132753573f6
 ┃ ┃ ┣ 📂82
 ┃ ┃ ┃ ┗ 📜41d2f67e5d6093307ff5bb334936ad7d10b5f0
 ┃ ┃ ┣ 📂84
 ┃ ┃ ┃ ┗ 📜0c20de339285e8adb632422a4702bfe7b22a24
 ┃ ┃ ┣ 📂87
 ┃ ┃ ┃ ┗ 📜06a00b1274e36b47a9d5b14cf5fdc7033c000e
 ┃ ┃ ┣ 📂89
 ┃ ┃ ┃ ┗ 📜67a973d182295d8f97f23091b48dd301003ca6
 ┃ ┃ ┣ 📂8a
 ┃ ┃ ┃ ┗ 📜9d6e9b63c9a9e7938699b7042d00cf4ebad694
 ┃ ┃ ┣ 📂91
 ┃ ┃ ┃ ┗ 📜710fb2aeb2b1d64f7e9735e72d2173adc1f27b
 ┃ ┃ ┣ 📂92
 ┃ ┃ ┃ ┗ 📜9322c4ac0e586ea7291fc3af5f424c9528daf1
 ┃ ┃ ┣ 📂93
 ┃ ┃ ┃ ┗ 📜83bfd9ba80ed14423ac0449a612d0c4c8eda7a
 ┃ ┃ ┣ 📂95
 ┃ ┃ ┃ ┗ 📜40c314256930667e4675260c4cd291f7981b5f
 ┃ ┃ ┣ 📂96
 ┃ ┃ ┃ ┗ 📜cd7ad1c3cc55cb88355d08e7596105a0cf4758
 ┃ ┃ ┣ 📂9b
 ┃ ┃ ┃ ┗ 📜3fc5a44939430bfb326ca9a33f80e99b06b5be
 ┃ ┃ ┣ 📂a0
 ┃ ┃ ┃ ┗ 📜bd2c72b1b2af513ea0d53b8f639bf9fce02590
 ┃ ┃ ┣ 📂a3
 ┃ ┃ ┃ ┣ 📜66ae000a47183c7ccf9b3aefe3ea5242a7c152
 ┃ ┃ ┃ ┣ 📜9edceeac5e22dc455d3c9adf4c8dcba8ed6140
 ┃ ┃ ┃ ┗ 📜a52406394476d2031f7566b15723f6c20b64b3
 ┃ ┃ ┣ 📂ab
 ┃ ┃ ┃ ┗ 📜1cd4a0fa5374e2037849da9e835d0362520adf
 ┃ ┃ ┣ 📂b2
 ┃ ┃ ┃ ┣ 📜180870b552f76189f27d3ee45f041dd0d176b1
 ┃ ┃ ┃ ┗ 📜60292df0fbdf12135a1057a789ee106521379c
 ┃ ┃ ┣ 📂b4
 ┃ ┃ ┃ ┗ 📜97d000ff20af3604afa5311402a42948a694d8
 ┃ ┃ ┣ 📂b6
 ┃ ┃ ┃ ┗ 📜f8653721b4325b639fdba924ba7740845da4ab
 ┃ ┃ ┣ 📂b7
 ┃ ┃ ┃ ┗ 📜bfee6e2096ac9d7c58c0211a6591dc6202de59
 ┃ ┃ ┣ 📂b9
 ┃ ┃ ┃ ┗ 📜a3ecb0ebf7c8f12c7e845bf6777ff538c75434
 ┃ ┃ ┣ 📂bb
 ┃ ┃ ┃ ┗ 📜082b8e8c40cb51067a212e739d9beeafa0841a
 ┃ ┃ ┣ 📂bc
 ┃ ┃ ┃ ┗ 📜47ec06527ac34600fa1f90c1bfc9527624929e
 ┃ ┃ ┣ 📂bd
 ┃ ┃ ┃ ┣ 📜316d3c3dbc4cea12db0ceb0f19989ff99a7fcc
 ┃ ┃ ┃ ┗ 📜a16f08ccc8e22e9318968189f666fe148e8b4a
 ┃ ┃ ┣ 📂be
 ┃ ┃ ┃ ┣ 📜f0ec55edd2f49cece6ef3ba06f4337c804ee84
 ┃ ┃ ┃ ┗ 📜fee97838579462db21ab00053aa72a333324b8
 ┃ ┃ ┣ 📂bf
 ┃ ┃ ┃ ┗ 📜b3e64ce378aed7ff0c401921df552b61f2c920
 ┃ ┃ ┣ 📂c3
 ┃ ┃ ┃ ┗ 📜ec82e8d48fb9037265cdf84a1d39b2a6ac1ca7
 ┃ ┃ ┣ 📂c8
 ┃ ┃ ┃ ┗ 📜1c52be3b15fcf211e5e1fe3f37dfef27dd1686
 ┃ ┃ ┣ 📂c9
 ┃ ┃ ┃ ┗ 📜bc452c27724f2e18dfaee0eabf17828a0608e3
 ┃ ┃ ┣ 📂cf
 ┃ ┃ ┃ ┣ 📜48961701c067731a1ed340febb80421faf2c7a
 ┃ ┃ ┃ ┗ 📜e18e3d97c0cb0f265f7506ec232902ad46ed92
 ┃ ┃ ┣ 📂d0
 ┃ ┃ ┃ ┣ 📜49173414ca4ccd193bda8e1baea93a0f8076eb
 ┃ ┃ ┃ ┗ 📜cbf18bb8fcb0ccf9eacdcb98ea4da7ed23ee54
 ┃ ┃ ┣ 📂d1
 ┃ ┃ ┃ ┣ 📜2f41760a2b08b21d519b89e010183c03809a39
 ┃ ┃ ┃ ┗ 📜b89f3feb6a5ddac59419e049f50e015a18de07
 ┃ ┃ ┣ 📂d3
 ┃ ┃ ┃ ┗ 📜a63ccab64da3be624aa38bfffc892eba4b0119
 ┃ ┃ ┣ 📂d5
 ┃ ┃ ┃ ┗ 📜935e6c0af117533f370084394437108d125c8b
 ┃ ┃ ┣ 📂db
 ┃ ┃ ┃ ┗ 📜275c363022311f1b327f57e249de2138d29992
 ┃ ┃ ┣ 📂dd
 ┃ ┃ ┃ ┗ 📜cbf52345008c41eb79fba6f7daa649ef9d797a
 ┃ ┃ ┣ 📂df
 ┃ ┃ ┃ ┗ 📜8c3c10b073ca3bdcb51822ddd32861822b756f
 ┃ ┃ ┣ 📂e1
 ┃ ┃ ┃ ┗ 📜893da5addd7de8433e257e1b151eb63b8fa15b
 ┃ ┃ ┣ 📂e3
 ┃ ┃ ┃ ┗ 📜358c74b43f9b44bb9da4cb36b753775b44d193
 ┃ ┃ ┣ 📂e6
 ┃ ┃ ┃ ┣ 📜1fa903936b6783128e7083c5d3266369cb1256
 ┃ ┃ ┃ ┣ 📜529d8023faed6a0185d91afdf6fee437fb520f
 ┃ ┃ ┃ ┣ 📜893fb742ff0b35beed6c9903778bedb7af2a99
 ┃ ┃ ┃ ┗ 📜9de29bb2d1d6434b8b29ae775ad8c2e48c5391
 ┃ ┃ ┣ 📂e7
 ┃ ┃ ┃ ┗ 📜e792d1b6c529dfd618961e4dcca7b6f34e2a79
 ┃ ┃ ┣ 📂e8
 ┃ ┃ ┃ ┗ 📜e60a9ce1d5561663e1d489b5357293d44ac1e8
 ┃ ┃ ┣ 📂e9
 ┃ ┃ ┃ ┗ 📜f70157fbf013977e1ca94440f8be614d27d40a
 ┃ ┃ ┣ 📂ec
 ┃ ┃ ┃ ┗ 📜34b6b728c868de9857cf8e3e18cb3dd355f18b
 ┃ ┃ ┣ 📂ed
 ┃ ┃ ┃ ┗ 📜05814351b77b552df3f2bda3f9f56d21a3e4e7
 ┃ ┃ ┣ 📂ee
 ┃ ┃ ┃ ┗ 📜306df99f956a524b7202cffd26fe8686e1a6b4
 ┃ ┃ ┣ 📂ef
 ┃ ┃ ┃ ┗ 📜e095120d4d7b1ebe06d0b7e9599f25fe904e29
 ┃ ┃ ┣ 📂f0
 ┃ ┃ ┃ ┣ 📜4a270847c5a2fb6145adb9b4f07deac3bceedc
 ┃ ┃ ┃ ┗ 📜f13b10978cb6c1fa17caf3552ebd070806fab7
 ┃ ┃ ┣ 📂f1
 ┃ ┃ ┃ ┗ 📜7ed0414924f8d843f8d7cc2c4927f85e190c7f
 ┃ ┃ ┣ 📂f2
 ┃ ┃ ┃ ┗ 📜57a1e471d03614ffe7c20a8f528ee3446d2e8b
 ┃ ┃ ┣ 📂f4
 ┃ ┃ ┃ ┗ 📜bc79bb03d78a1db008560226ffbdbc0b4c01fb
 ┃ ┃ ┣ 📂fa
 ┃ ┃ ┃ ┣ 📜57884f575c7d6a6175c04c272bc6bf83767700
 ┃ ┃ ┃ ┗ 📜8b16231413e7d752ec498fe67eb4c8d7e9e1b4
 ┃ ┃ ┣ 📂fe
 ┃ ┃ ┃ ┗ 📜a93043d2ec17d0008f0730f9b203aefcb087f8
 ┃ ┃ ┣ 📂info
 ┃ ┃ ┗ 📂pack
 ┃ ┣ 📂refs
 ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┗ 📜master
 ┃ ┃ ┣ 📂remotes
 ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┗ 📜master
 ┃ ┃ ┗ 📂tags
 ┃ ┣ 📜COMMIT_EDITMSG
 ┃ ┣ 📜config
 ┃ ┣ 📜description
 ┃ ┣ 📜HEAD
 ┃ ┗ 📜index
 ┣ 📂Movie_files
 ┃ ┣ 📜2e59b04d5cc4e282fb1eed34620ba6800c931049.js.다운로드
 ┃ ┣ 📜58582148
 ┃ ┣ 📜admin.scss
 ┃ ┣ 📜after.js.다운로드
 ┃ ┣ 📜analytics.js.다운로드
 ┃ ┣ 📜before.js.다운로드
 ┃ ┣ 📜button.scss
 ┃ ┣ 📜common.scss
 ┃ ┣ 📜erd-icons.scss
 ┃ ┣ 📜f.txt
 ┃ ┣ 📜facebook_login_button.css
 ┃ ┣ 📜forms.scss
 ┃ ┣ 📜github_login_button.css
 ┃ ┣ 📜google_login_button.css
 ┃ ┣ 📜homepage.scss
 ┃ ┣ 📜icon
 ┃ ┣ 📜like.html
 ┃ ┣ 📜login_buttons.less
 ┃ ┣ 📜OqOE21UvWe3.png
 ┃ ┣ 📜reporters.js.다운로드
 ┃ ┣ 📜sdk.js(1).다운로드
 ┃ ┣ 📜sdk.js.다운로드
 ┃ ┣ 📜symbol-es6.min.js.다운로드
 ┃ ┣ 📜tracer.js.다운로드
 ┃ ┣ 📜utils.js.다운로드
 ┃ ┣ 📜variables.scss
 ┃ ┗ 📜zone.js.다운로드
 ┣ 📂revue
 ┃ ┣ 📂accounts
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0002_user_followers.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0003_auto_20200611_1939.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0004_auto_20200613_1536.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┣ 📜0002_user_followers.py
 ┃ ┃ ┃ ┣ 📜0003_auto_20200611_1939.py
 ┃ ┃ ┃ ┣ 📜0004_auto_20200613_1536.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┗ 📂accounts
 ┃ ┃ ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┃ ┃ ┣ 📜profile.html
 ┃ ┃ ┃ ┃ ┣ 📜update.html
 ┃ ┃ ┃ ┃ ┗ 📜user_activate_email.html
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜admin.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜forms.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜models.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜tokens.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜urls.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜views.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜tokens.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂community
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0002_auto_20200611_1612.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0003_auto_20200613_1536.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0004_auto_20200613_1607.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0005_report_reported_at.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0006_auto_20200614_1525.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0007_auto_20200614_1531.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┣ 📜0002_auto_20200611_1612.py
 ┃ ┃ ┃ ┣ 📜0003_auto_20200613_1536.py
 ┃ ┃ ┃ ┣ 📜0004_auto_20200613_1607.py
 ┃ ┃ ┃ ┣ 📜0005_report_reported_at.py
 ┃ ┃ ┃ ┣ 📜0006_auto_20200614_1525.py
 ┃ ┃ ┃ ┣ 📜0007_auto_20200614_1531.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┗ 📂community
 ┃ ┃ ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┃ ┃ ┣ 📜report.html
 ┃ ┃ ┃ ┃ ┣ 📜review_detail.html
 ┃ ┃ ┃ ┃ ┣ 📜review_list.html
 ┃ ┃ ┃ ┃ ┣ 📜shortform.html
 ┃ ┃ ┃ ┃ ┣ 📜shortreviewList.html
 ┃ ┃ ┃ ┃ ┗ 📜shortreview_detail.html
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜admin.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜forms.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜models.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜urls.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜views.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂movies
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┣ 📜0001_initial.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0002_trending.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0003_auto_20200611_1942.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0004_auto_20200611_2110.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0005_auto_20200611_2114.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0006_movie_tags.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0007_auto_20200613_1957.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0008_auto_20200613_2057.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┣ 📜0009_auto_20200613_2339.cpython-38.pyc
 ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┣ 📜0002_trending.py
 ┃ ┃ ┃ ┣ 📜0003_auto_20200611_1942.py
 ┃ ┃ ┃ ┣ 📜0004_auto_20200611_2110.py
 ┃ ┃ ┃ ┣ 📜0005_auto_20200611_2114.py
 ┃ ┃ ┃ ┣ 📜0006_movie_tags.py
 ┃ ┃ ┃ ┣ 📜0007_auto_20200613_1957.py
 ┃ ┃ ┃ ┣ 📜0008_auto_20200613_2057.py
 ┃ ┃ ┃ ┣ 📜0009_auto_20200613_2339.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂templates
 ┃ ┃ ┃ ┗ 📂movies
 ┃ ┃ ┃ ┃ ┣ 📜choicegenre.html
 ┃ ┃ ┃ ┃ ┣ 📜detail.html
 ┃ ┃ ┃ ┃ ┣ 📜firstchoice.html
 ┃ ┃ ┃ ┃ ┣ 📜index.html
 ┃ ┃ ┃ ┃ ┣ 📜mainpage.html
 ┃ ┃ ┃ ┃ ┗ 📜search.html
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜admin.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜models.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜urls.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜views.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂revue
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜settings.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜urls.cpython-38.pyc
 ┃ ┃ ┃ ┣ 📜wsgi.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-38.pyc
 ┃ ┃ ┣ 📜settings.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜wsgi.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂static
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┣ 📜default.css
 ┃ ┃ ┃ ┗ 📜style.css
 ┃ ┃ ┗ 📂image
 ┃ ┃ ┃ ┣ 📜mainpageHeader.jpg
 ┃ ┃ ┃ ┣ 📜null_image.jpg
 ┃ ┃ ┃ ┗ 📜titleicon.ico
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📜base.html
 ┃ ┣ 📜db.sqlite3
 ┃ ┣ 📜genres.json
 ┃ ┣ 📜manage.py
 ┃ ┣ 📜movies.json
 ┃ ┣ 📜movies2.json
 ┃ ┗ 📜movies3.json
 ┣ 📜.gitignore
 ┣ 📜KakaoTalk_20200612_231945914.png
 ┣ 📜Movie.html
 ┣ 📜README.md
 ┗ 📜requirement.txt
```

