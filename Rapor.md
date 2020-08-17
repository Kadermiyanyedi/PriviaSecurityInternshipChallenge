## Privia Security Staj Uygulaması Raporu
#### Kader Miyanyedi
---
* Daha önce python/django deneyimim olduğu için verilen görevi django ile yapma kararı aldım.

* Projeye ilk başladığımda modellerimi oluşturdum. Modelleri veritabanındaki tablolar olarak düşünebilirsiniz. Blog postlarına yorum yapılabilmesi için, post ile yorumlar arasında bir foreign key belirledim. Bu sayede yorumların hangi posta ait olacağını biliyor olacaktım.

* Django ile hazır bir admin paneli gelmektedir. admin.py üzerinde birkaç ekleme yaparak modellerimizi bu panelde görmek mümkündür. Modelleri oluşturduktan sonra admin panelini düzenledim. Bu sayede modellerimle ilgili verileri admin panelinden inceleyebilir,düzenleyebilir ve filtreleyebiliyor olacaktım.

* Modellerimizden yeni bir obje ürettiğimizde bu objeler admin panelinde Blog object(2) gibi görünmektedir. Ancak bu şekilde postlar hakkında bilgi edinmek oldukça güçtür. Bu sebeple models.py içerisinde ` __str__() ` fonksiyonunu ezerek yeni bir obje oluştuğunda return etmesi gereken ifadeyi belirledim.

* Api ve blog klasörleri altında iki farklu urls.py dosyası görülmekte. Django gelen isteğe uygun gördüğü ilk urle girmekte ve onu çalıştırmayı denemektedir. Fakat büyük bir projede birden çok urli tek bir url dosyasında biriktirmek hem bir sorunda güncellemeyi zorlaştırır hem de çakışmalar meydana gelebilir ve yanlış bir view görüntülenebilir. Bu sebeple her uygulamaya ait olan urller kendi içerisinde bulundurmak ve ana url listesine include etmek çok daha kullanışlıdır. Bende projede bunu göz önüne alarak url dosyalarımı ayırdım.

* Templates html uzantılı dosyalarımızın bulunduğu klasörlerimizdir. Burada block/endblock yapısını kullandım. Örneğin bir sayfanın header kısmı her zaman aynıdır. İçerik değişse bile header kısmı değişmez. Her yazmış olduğumuz html dosyası içerisinde yeniden header eklemek yerine bu yapıyı kullanabiliriz. Bu yapı sayesinde bir htmlin bellirli kısımlarını(bizim projemizde içerik kısmı) değiştirerek kullanma imkanına sahibiz. Projemde bu yapıyı kullanarak gereksiz kod yazımından sakındım.

* Django form konusunda birden çok yönteme sahip. Ben bunlar arasında ModelForm yapısını kullanmayı tercih ettim. Bu yapı modelimizi almakta ve bizim belirtiğimiz fieldlere göre bir form oluşturmaktadır.Kullanım olarak bana daha kısa,öz ve işlevsel geldiği için bu form yapısını tercih ettim.

* View yapısı olarak tek bir functional view,ve birden çok class based view kullandım. Class based view kod okunurluğunu zorlasada, daha fazla işlevsellik için genişletebilir olması,daha az satırda aynı işlemleri yapabiliyor olmak oldukça iyi bir durum. Her iki yapıdanda bir örnek olmasını istediğim için bir adet functional view ekledim.

* Sayfada çok fazla post eklendiğinde hepsi alt alta olmasın diye sayfalama özelliği ekledim, ve her sayfada 2 post görülmesi şeklinde ayarladım.

* Formlarımın html kısımlarında güzel bir görüntü oluşturması açısından ayrıca crispy forms kullandım.

* Post title göre arama yapabilme özelliği ekledim. Djangoda filtreleme için üçüncü parti bir uygulama olan django-filter kullanımıda oldukça yaygın fakat ben djangonun özellikleri ile kendi search viewımı yazmayı tercih ettim. Bunu seçmemdeki ana sebep ufak uygulamalarımda django içinde kendi özellikleri ile yapabileceğim basit işlemler için üçüncü parti bir uygulama kullanarak bağımlılıkları artırmak istemedim.

* Projeme aynı zamanda django rest framework ekledim. DRF frontend kısmında api isteklerinde bulunurken kolaylık sağlayacak.

* Ayrıca projemde swagger ekledim. localhost:8000/swagger adresine gidildiğinde api ile ilgili yapılabilecek http istekleri, modeller ve içerisindeki fieldlar hakkında bilgi edinebilir ve postman,curl gibi başka bir araç kullanmadan http isteklerinde bulunup apiyi test edebilirsiniz. Farklı bir araç kullanmaktansa swagger ile test yapmak bana daha kullanışlı gelmekte ve api hakkında geniş bilgiler sunmaktadır.