  ________  ___________   _____    ____  ___________ ___    ____                                   
 /_  __/ / / / ____/   | / ___/   / __ )/ ____/ ___//   |  / __ \                                  
  / / / / / / / __/ /| | \__ \   / __  / __/  \__ \/ /| | / /_/ /                                  
 / / / /_/ / /_/ / ___ |___/ /  / /_/ / /___ ___/ / ___ |/ _, _/                                   
/_/ _\\___/\\___/_/  \\\\\__/ _\\\__\\\____\\\\__/_/__\\\\\_\\\_____  __  ___________________  ____
   /   |  / /       / /   |  / __ )/   |  / __ \   / ____/ ____/ __ \/  |/  / ____/_  __/ __ \/  _/
  / /| | / /   __  / / /| | / __  / /| | / /_/ /  / / __/ __/ / / / / /|_/ / __/   / / / /_/ // /  
 / ___ |/ /___/ /_/ / ___ |/ /_/ / ___ |/ _, _/  / /_/ / /___/ /_/ / /  / / /___  / / / _, _// /   
/_/  |_/_____/\____/_/  |_/_____/_/  |_/_/ |_|   \____/_____/\____/_/  /_/_____/ /_/ /_/ |_/___/   
                                                                                                   
#===============================================================================================#
#	README.txt										#
#===============================================================================================#
#	Tugas Besar - Aljabar Geometri								#
#	"Simulasi Transformasi Linier pada Bidang 2D dan 3D dengan Menggunakan OpenGL API"	#
#												#
#	Bahasa Pemrograman yang digunakan: Python						#
#-----------------------------------------------------------------------------------------------#
#	Anggota Kelompok:									#
#												#
#	Abda Shaffan Diva	-	13517021						#
#	Aidil Rezjki S		-	13517070						#
#	Taufikurrahman Anwar	-	13517074						#
#===============================================================================================#
#	Apa saja yang ada di folder tugas besar ini?						#
#-----------------------------------------------------------------------------------------------#
#	Di folder induk, terdapat tiga folder yaitu:						#
#	- bin											#
#	- doc											#
#	- src											#
#												#
#	Pada folder bin terdapat file executable yang merupakan hasil kompilasi dari program	#
#	tugas besar ini.									#
#	Pada folder doc terdapat beberapa file yaitu laporan tugas besar ini, spesifikasi tugas	#
#	besar ini, dan file README.txt.								#
#	Pada folder src terdapat kode sumber dari tugas besar ini, yang ditulis dalam bahasa	#
#	pemrograman Python.									#
#===============================================================================================#
#	Bagaimana cara menjalankan program tugas besar ini?					#
#-----------------------------------------------------------------------------------------------#
#	Program tugas besar ini dapat dijalankan dengan dua cara. Cara yang pertama adalah	#
#	dengan menjalankan file executable yang ada di folder bin.				#
#												#
#	Namun file tersebut belum tentu dapat dijalankan di semua sistem operasi, maka terdapat	#
#	cara kedua untuk menjalankan program ini.						#
#	Cara yang kedua adalah dengan melakukan kompilasi pada kode sumber yang terdapat pada	#
#	folder src. Langkah-langkah untuk melakukan kompilasi adalah sebagai berikut.		#
#												#
#	1. Pastikan Python sudah terinstall di komputer anda. Kalau belum, silahkan melakukan	#
#	   instalasi sesuai dengan sistem operasi anda.						#
#	2. Buka terminal atau command prompt ataupun powershell di folder src.			#
#	3. Jalankan perintah berikut tanpa tanda kutip:						#
#		"python main.py"								#
#	4. Setelah itu, program tugas besar ini akan dijalankan di komputer anda.		#
#												#
#===============================================================================================#
#	Apa saja yang dapat dilakukan oleh program ini?						#
#-----------------------------------------------------------------------------------------------#
#	Pada program untuk tugas besar kali ini, dibuat sebuah program yang menggunakan OpenGL	#
#	untuk melakukan transformasi linier di ruang 2D dan 3D.					#
#												#
#	Terdapat dua mode pada program ini, yaitu mode 2D dan 3D.				#
#												#
#	Pada mode 2D terdapat kontrol program yaitu dengan menggunakan tombol berikut.		#
#		1. Z, X		:	Melakukan zoom pada kamera.				#
#		2. Arrow Keys	:	Melakukan pan pada kamera.				#
#												#
#	Pada mode 3D terdapat kontrol program yaitu dengan menggunakan tombol berikut.		#
#		1. W, S		:	Rotasi kamera terhadap sumbu x.				#
#		2. A, D		:	Rotasi kamera terhadap sumbu y.				#
#		3. Z, X		:	Melakukan zoom pada kamera.				#
#		4. Arrow Keys	:	Melakukan pan pada kamera.				#
#	Kontrol Kamera										#
#		1. W, S		:	Rotasi kamera terhadap sumbu x.	(Hanya pada mode 3D).	#
#		2. A, D		:	Rotasi kamera terhadap sumbu y.	(Hanya pada mode 3D).	#
#		3. Z, X		:	Melakukan zoom pada kamera.				#
#		4. Arrow Keys	:	Melakukan pan pada kamera.				#
#												#
#		Pada mode 2D, pengguna pertama kali akan diminta untuk memasukkan jumlah titik	#
#	dan titik tersebut pada bidang kartesian 2D. Dianjurkan agar pengguna memasukkan titik	#
#	searah jarum jam ataupun berlawanan jarum jam (tidak acak-acakan).			#
#		Selanjutnya program akan membuka sebuah window baru yang merupakan gambar dari	#
#	bidang kartesian 2D dan bangun 2D sesuai dengan titik yang telah dimasukkan pengguna	#
#	sebelumnya.										#
#		Setelah itu, program dapat menerima perintah dari pengguna untuk melakukan	#
#	transformasi linier dan juga beberapa hal lainnya. Program akan menampilkan animasi	#
#	sesuai dengan perintah dari pengguna. Adapun perintah-perintah tersebut adalah sebagai	#
#	berikut.										#
#												#
#		1. translate <dx> <dy>								#
#			Melakukan translasi objek dengan menggeser sesuai dengan dx dan dy.	#
#		2. dilate <k>									#
#			Melakukan dilatasi objek dengan faktor k.				#
#		3. rotate <deg> <a> <b>								#
#			Melakukan rotasi pada objek sebanyak deg (dalam derajat) terhadap	#
#			titik (a, b).								#
#		4. reflect <param>								#
#			Melakukan pencerminan objek terhadap beberapa hal sesuai parameter.	#
#			Parameter x:								#
#				Terhadap sumbu x.						#
#			Parameter y:								#
#				Terhadap sumbu y.						#
#			Parameter y=x:								#
#				Terhadap garis y = x.						#
#			Parameter y=-x:								#
#				Terhadap garis y = -x.						#
#			Parameter a b:								#
#				Terhadap titik (a, b).						#
#		5. shear <param> <k>								#
#			Melakukan operasi shear pada objek dengan faktor k.			#
#				Parameter x:							#
#					Operasi pada sumbu x.					#
#				Parameter y:							#
#					Operasi pada sumbu y.					#
#		6. stretch <param> <k>								#
#			Melakukan operasi stretch pada objek dengan faktor k.			#
#				Parameter x:							#
#					Operasi pada sumbu x.					#
#				Parameter y:							#
#					Operasi pada sumbu y.					#
#		7. custom <a> <b> <c> <d>							#
#			Melakukan transformasi linier pada objek sesuai matriks transformasi	#
#				|a	b|							#
#				|c	d|							#
#		8. multiple									#
#			Menerima perintah dari pengguna secara beruntun.			#
#		9. reset									#
#			Mengembalikan objek menjadi semula, yaitu saat awal sebelum dilakukan	#
#			transformasi linier pada objek.						#
#		10. exit									#
#			Keluar dari program.							#
#												#
#		Selain transformasi di ruang 2D, program ini juga dapat melakukan transformasi	#
#	di ruang 3D, yaitu pada mode 3D. Pada mode 3D, semua perintah sebelumnya dapat juga	#
#	dilakukan, dengan sedikit perubahan. Namun, perbedaan dari mode 3D dengan 2D adalah	#
#	bentuk objek yang terbatas, yaitu hanya sebuah kubus. Adapun perintah-perintah yang	#
#	dapat dijalankan pada mode 3D adalah sebagai berikut.					#
#												#
#		1. translate <dx> <dy> <dy>							#
#			Melakukan translasi objek dengan menggeser sesuai dengan dx, dy. dan dz.#
#		2. dilate <k>									#
#			Melakukan dilatasi objek dengan faktor k.				#
#		3. rotate <param> <deg>								#
#			Parameter x:								#
#				Melakukan rotasi pada objek sebanyak deg (dalam derajat)	#
#			terhadap sumbu x.							#
#			Parameter y:								#
#				Melakukan rotasi pada objek sebanyak deg (dalam derajat)	#
#			terhadap sumbu y.							#
#			Parameter z:								#
#				Melakukan rotasi pada objek sebanyak deg (dalam derajat)	#
#			terhadap sumbu z.							#
#		4. reflect <param>								#
#			Melakukan pencerminan objek terhadap beberapa hal sesuai parameter.	#
#			Parameter x:								#
#				Terhadap sumbu x.						#
#			Parameter y:								#
#				Terhadap sumbu y.						#
#			Parameter z:								#
#				Terhadap sumbu z.						#
#			Parameter a b:								#
#				Terhadap titik (a, b).						#
#		5. shear <param> <k>								#
#			Melakukan operasi shear pada objek dengan faktor k.			#
#				Parameter x:							#
#					Operasi pada sumbu x.					#
#				Parameter y:							#
#					Operasi pada sumbu y.					#
#				Parameter z:							#
#					Operasi pada sumbu y.					#
#		6. stretch <param> <k>								#
#			Melakukan operasi stretch pada objek dengan faktor k.			#
#				Parameter x:							#
#					Operasi pada sumbu x.					#
#				Parameter y:							#
#					Operasi pada sumbu y.					#
#				Parameter z:							#
#					Operasi pada sumbu z.					#
#		7. custom <a> <b> <c> <d> <e> <f> <g> <h> <i>					#
#			Melakukan transformasi linier pada objek sesuai matriks transformasi	#
#				|a	b	c|						#
#				|d	e	f|						#
#				|g	h	i|						#
#		8. multiple									#
#			Menerima perintah dari pengguna secara beruntun.			#
#		9. reset									#
#			Mengembalikan objek menjadi semula, yaitu saat awal sebelum dilakukan	#
#			transformasi linier pada objek.						#
#		10. exit									#
#			Keluar dari program.							#
#												#
#===============================================================================================#	
#	SEKIAN DAN TERIMA KASIH									#
#===============================================================================================#
