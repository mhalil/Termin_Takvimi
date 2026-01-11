# Termin Takvimi

Partiler halinde alım yapılan mazlemelerin takibi ve işlerin detaylarını görmek için kullanılabilecek HTML tabanlı takvim uygulaması.
Gemini'a taleplerimi ileterek kodlattığım web uygulamasını, istifadenize sunuyorum.

# Uygulamanın Özellikleri

* **index.html** dosyası çalıştırıldığında aşağıdaki gibi bir takvim ile karşılaşıyoruz. **Bugün** bilgisi, takvim üzerindeki açık sarı arkaplan rengi ile temsil ediliyor.

![SS_01.png](img/SS_01.png)

* Takvim uygulaması (index.html) çalıştırıldığında, üzerindeki tüm veriyi aynı dizindeki **veriler.js isimli JSON**  dosyasından alıyor/okuyor.
* Takvim üzerindeki bilgilerden birine tıklandığında açılır pencere içinde İhaleye ait detaylar görüntüleniyor. Örneğin 2 Ocaktaki işe tıkladığımızda aşağıdaki pencere açılıyor. Bugün 10 Ocak olduğu için tıkladığımız termin bilgisi kırmızı arkaplan rengi ile gösteriliyor ve "PARTİ TESLİM SÜRESİ GEÇTİ" bilgisi yazıyor.

![SS_02.png](img/SS_02.png)

* **Tümünü Gör** butonuna basıldığında ise Geçerli iş ve yükleniciye ait detaylar görünüyor. Geçmiş tarihli parti bilgileri kırmızı renkli olarak gösterilir.

![SS_03.png](img/SS_03.png)

* Takvimde ileri tarihli bir işe/partiye ait bilgiye tıklarsak (örneğin 24 Ocak) açılan PARTİ BİLGİSİ penceresinde "PARTİ TESLİM ZAMANI" yazısını ve arkaplanın yeşil olduğunu görürsünüz. 

![SS_04.png](img/SS_04.png)

* **Tümünü Gör** butonuna basıldığında ise Geçerli iş ve yükleniciye ait detaylar görünüyor.

![SS_05.png](img/SS_05.png)

* Ana sayfanın sol üst kısmındaki **OK Tuşları (🡄 🡆)** ile aylar arasında gezinebilir, **BUGÜN** butonu ile de güncel güne ait aya dönebilirsiniz. Örneğin Ok tuşu ile Mart ayına gelip o aya ait iş ve parti bilgilerini görebiliri. 

![SS_06.png](img/SS_06.png)

* Ya da Sol Ok tuşu ile geri gidip Şubat Ayı verilerini **AJANDA** görünümünde liste halinde görebiliriz.

![SS_07.png](img/SS_07.png)

* **AJANDA** görünümündeyken **PDF/YAZDIR** butonuna tıklayarak o ayki faaliyetleri kolayca çıktı alacak hale getirebilir ya da yazdırabiliriz.

![SS_08.png](img/SS_08.png)

* Takvimin **AY** görünümüne geçerek **BUGÜN** butonuna basıyor ve ay içindeki işleri / partileri görüyoruz.

![SS_09.png](img/SS_09.png)

* Takvimin **AY** görünümüne geçerek **BUGÜN** butonuna basıyor ve ay içindeki işleri / partileri görüyoruz. Sol Kısımdaki "**TAMAMLANAN**" bilgi kartına tıkladığımızda, Ocak ayında tamamlanan iş olmadığı için tüm takvim boş kalıyor.

![SS_10.png](img/SS_10.png)

* **SOL OK** tuşu ile **Kasım** ayına geldiğimizde **DEVAM EDEN** ve **TAMAMLANAN** tüm işleri, takvim üzerinde görüyoruz. 

![SS_11.png](img/SS_11.png)

* Sol kısımdan **DEVAM EDEN** bilgi kartına tıklayınca, Takvimde sadece Kasım ayında devam eden işler gösterilir. Biten işle gizlenir. 

![SS_12.png](img/SS_12.png)

* Sol kısımdaki **FİRMA BAZLI** listesinden bir firma seçilirse, hem  **İHALE BAZLI** listesinde hem de takvim içerisinde sadece seçilen Firmaya ait işler listelenir / gösterilir.

![SS_13.png](img/SS_13.png)

* **FİRMA BAZLI** açılır menüsünden seçim yaptık ve takvim içeriğinde sadece seçili işe ait bilgiler gösterildi.

![SS_14.png](img/SS_14.png)

* **İHALE BAZLI** açılır menüsünde de sadece seçili firmaya ait işler listelendi.

![SS_15.png](img/SS_15.png)

* **FİRMA BAZLI** açılır menüsünden seçim yaptıktan sonra **DEVAM EDEN** bilgi kartına tıkladığımızda, sadece seçili firmaya ait devam eden işlerin detay bilgileri görüntülenir.

![SS_16.png](img/SS_16.png)

* Doğal olarak, **FİRMA BAZLI** açılır menüsünden seçim yapılmış iken **TAMAMLANAN** bilgi kartına tıkladığımızda da, sadece seçili firmaya ait tamamlanan işlerin detay bilgileri görüntülenir. Tamamlanan iş yoksa aşağıdaki gibi bilgi ile karşılaşırsınız.

![SS_17.png](img/SS_17.png)

* **FİRMA BAZLI** listesinden yeni bir firma seçelim takvimde, diğer işler gizlendi.

![SS_18.png](img/SS_18.png)

* **DEVAM EDEN** işlerinin detaylarını inceleyelim. 

![SS_19.png](img/SS_19.png)

* Aynı firmanın **TAMAMLANAN** İşlerinin detaylarını inceleyelim.

![SS_20.png](img/SS_20.png)

* **AY** görünümünden farklı olarak **AJANDA** görünümünde, aylık iş/parti bilgileri liste şeklinde görüntülenebilir.

![SS_21.png](img/SS_21.png)

* **AY** görünümünde olduğu gibi **AJANDA** görünümünde de tüm işler ya da **FİRMA BAZLI** menüsünden seçim yapılarak bir firmaya ait işler filtrelenebilir/ görüntülenebilir.

![SS_22.png](img/SS_22.png)

* Takvim uygulamasının güzel ve kullanışlı bir özelliği de yeni İhale bilgileri ekleme ya da mevcut ihale bilgilerini Düzenlemeye / Silmeye imkan tanımasıdır. Sol kısımda bulunan **DÜZENLE / EKLE** butonuna basarak düzenleme sayfasını görüntüleyebiliriz.

![SS_23.png](img/SS_23.png)

* **Dosya Seç** butonu yardımı ile mevcut ihale bilgilerinin bulunduğu dosyayı seçelim.

![SS_24.png](img/SS_24.png)

* Gördüğünüz gibi **JSON (.js)** dosyası yüklendi. Artık mevcut veriler üzerinde değişiklik yapabiliriz.

![SS_25.png](img/SS_25.png)

* Sayfanın en altına gelip son ihaleye ait bilgilere bakıyoruz. 

![SS_26.png](img/SS_26.png)

* Yeni işe ait bilgileri yazarak, uygulamanın,  otomatik olarak kayıt oluşturmasını sağlıyoruz. 

![SS_27.png](img/SS_27.png)

* Yeni işe ait bilgileri yazıp, **SİHİRBAZI ÇALIŞTIR** butonuna basarak uygulamanın, bizim için belirttiğimiz parti sayısı kadar kayıt oluşturmasını sağlıyoruz. Yazılan Sözleşme Tutarı, parti sayısına bölünerek, parti tutarları eşit olacak şekilde oluşturuluyor. İsterseniz sonrasında değerleri değiştirebilirsiniz.

![SS_28.png](img/SS_28.png)

* Sayfanın altına geldiğimizde yeni işe ait bilgilerin eklendiğini görüyoruz.

![SS_29.png](img/SS_29.png)

* **VERİLERİ JS OLARAK KAYDET** butonu yardımı ile de yaptığımız değişikliği  kaydetmek istiyoruz.

![SS_30.png](img/SS_30.png)

* Takvim uygulaması verileri **VERİLER.JS** dosyasından okuduğu için değişikliği aynı dosyanın üzerine kaydediyoruz.

![SS_31.png](img/SS_31.png)

* Sayfayı F5 tuşu ile yenilediğimizde, veriler yeniden okunuyor ve yeni eklenen işin uygulamaya dahil olduğunu görüyoruz.

![SS_32.png](img/SS_32.png)

* **FİRMA BAZLI** listesinde yeni işi seçip takvime filtre uyguluyoruz.

![SS_33.png](img/SS_33.png)

* **DEVAM EDEN** bilgi kartının yanındaki **GÖZ** simgesine tıklayarak yeni işin finansal detaylarını görüntülüyoruz.

![SS_34.png](img/SS_34.png)

* Firma Filtresi uygulamazsak DEVAM EDEN (AKTİF PROJEKSİYON) işlerin tamamına ait finansal detaylar görüntülenir.

![SS_35.png](img/SS_35.png)

* Sayfayı aşağı kaydırarak Devam eden işlerin listesini görebiliriz.

![SS_36.png](img/SS_36.png)

* Herhangi bir işe tıkladığımızda işe ait detaylar görüntülenir.

![SS_37.png](img/SS_37.png)

* **DEVAM EDEN (AKTİF PROJEKSİYON)** ekranında AY bilgisine tıklanırsa, o ay hangi firmaların kaçıncı partilerine ait ödeme yapılması gerektiğine dair detaylar da görüntülenir.

![SS_38.png](img/SS_38.png)

* Aynı özellikler **TAMAMLANAN** işler için de geçerlidir. **TAMAMLANAN** bilgi kartının yanındaki **GÖZ** simgesine tıklayarak, tamamlanan / biten işlerin ihale/iş detayları, toplam ödenen tutarları ve aylık detaylarını görüntüleyebiliriz.

![SS_39.png](img/SS_39.png)

* İstenilen **AY** kartına tıklayarak, o ay hangi firmaların hangi işlerinin kaçıncı partisine dair ödeme yapıldığını görebiliriz. 

![SS_40.png](img/SS_40.png)
