# Termin Takvimi

Partiler halinde alım yapılan mazlemelerin takibi ve işlerin detaylarını görmek için kullanılabilecek HTML tabanlı takvim uygulaması.
Gemini'a taleplerimi ileterek kodlattığım web uygulamasını, istifadenize sunuyorum.

# Uygulamanın Özellikleri

* **index.html** dosyası çalıştırıldığında aşağıdaki boş takvim ile karşılaşıyoruz. **Bugün** bilgisi, takvim üzerindeki açık sarı renk ile temsil edilir.

![SS_01.png](img/SS_01.png)

* **CSV** uzantılı **veri dosyası** seçildiğinde, dosya içeriğindeki bilgiler, takvimde ilgili yerlere yerleşiyor. Bilgi Kartları ve botunlarda bilgiler görüntüleniyor.

![SS_02.png](img/SS_02.png)

* **Tamamlanmış İşleri Gizle** seçeneği varsayılan olarak **aktif** olacak şekilde ayarlandığı için, mevcut devam eden işlere ait bilgi (İhale adı, Yüklenici adı ve Genel Özet) görüntüleniyor. Aşağıdaki resimde, **İhale Adı** açılır menüsünde sadece mevcut devam eden işlere ait bilgiler görüntüleniyor.

![SS_03.png](img/SS_03.png)

* Aşağıdaki resimde, **Yüklenici Firma** açılır menüsünde sadece mevcut devam eden işlere ait bilgiler görüntüleniyor.

![SS_04.png](img/SS_04.png)

* **Tamamlanmış İşleri Gizle** seçeneği **pasifleştirilirse**, CSV dosyasındaki biten işlere ait detaylar da (yani tüm veri) hem açılır menülerde, hem özet bilgilerde hem de takvimde gösterilir. Aşağıdaki resimde, **İhale Adı** açılır menüsünde tüm işlere ait bilgiler görüntüleniyor.

![SS_05.png](img/SS_05.png)

* Aşağıdaki resimde, **Yüklenici Firma** açılır menüsünde tüm işlere ait bilgiler görüntüleniyor. Bazı yüklenici firmaların hem biten hem de devam eden işleri olduğu için her halükarda menüde ismi görünür.

![SS_06.png](img/SS_06.png)

* **İhale  Adı** ya da **Yüklenici Firma** açılır menülerinden seçim yapılmadan **Kalan Termin Detaylarını Göster** butonuna tıklandığında tüm devam eden işlere (ihalelere) ait bilgilere görüntülenir.

![SS_07.png](img/SS_07.png)

* **Detayları Görüntüle** butonuna basılırsa, ilgili işin genel bilgilerinin yanında (İhale adı, Yüklenici Firma, İhale Kayıt Numarası, Sözleşme Tutarı), ihalenin toplam kaç partiden oluştuğu, parti son teslim tarihleri, bu tarihlerin geçip geçmediği ve parti tutarları görüntülenir.

![SS_08.png](img/SS_08.png)

* **Tamamlanmış İşleri Göster** butonuna tıklandığında, **İhale Adı** ve **Son partinin teslim tarihi** bilgileri liste görüntülenir.

![SS_09.png](img/SS_09.png)

* Listede herhangi bir İş seçilirse, ilgili işin genel bilgileri yani İhale adı, Yüklenici Firma, İhale Kayıt Numarası, Sözleşme Tutarı, ihalenin toplam kaç partiden oluştuğu, partilere ait son teslim tarihleri ve parti tutarları görüntülenir.

![SS_10.png](img/SS_10.png)

* Takvim üzerinde her iş (ihale) farklı bir renkte görüntülenir. Bir işe tıklandığında, o partiye ait detaylar görüntülenir.

![SS_11.png](img/SS_11.png)

* Takvim üzerindeki **ok tuşları** yardımıyla ileri tarihlere gidilerek devam edecek işlere/partilere  ait detaylar görüntülenebilir.

![SS_12.png](img/SS_12.png)

* Takvim üzerindeki **ok tuşları** yardımıyla geçmiş tarihlere gidilerek devam eden ya da biten işlere ait detaylar görüntülenebilir.

![SS_13.png](img/SS_13.png)

* **Yüklenici Firma** açılır menüsünden bir Yüklenici seçilirse, Takvim üzerinde sadece o Yükleniciye ait ihalelere ve parti bilgileri görüntülenir. Yani Yükleniciye filtre uygulanır. Aşağıdaki resimde, **Hassas Ölçüm San.  ve Tic. A.Ş**.'nin ihale ve parti bilgileri filtre uygulanarak gösterilmiştir. Filtreyi temizlemek için **Filtreleri Temizle** butonuna basılabilir.

![SS_14.png](img/SS_14.png)

* **İhale Adı** açılır menüsünden bir İhale seçilirse, Takvim üzerinde sadece o İhaleye ait parti bilgileri görüntülenir. Yani İhale Adına filtre uygulanır. Aşağıdaki resimde, **Pirinç Malzemeden Mamul Manşon Tip Bağlantı Parçası** İşine (ihalesine) filtre uygulanarak takvim bilgisi gösterilmiştir. Filtreyi temizlemek için **Filtreleri Temizle** butonuna basılabilir.

![SS_15.png](img/SS_15.png)

* Yüklenen CSV dosya ayarlarını değiştirebileceğiniz **CSV Sütun Yapılandırma Ayarları**nı gizleyip gösterebilirsiniz. Elinizdeki CSV dosyasının içeriğine göre, ayarları bu bölümden düzenleyebilirsiniz.

![SS_16.png](img/SS_16.png)

* Takvimde gösterilen İhale (iş) renklerini bu bölümden değiştirebilir / ayarlayabilirsiniz. İhale adına göre bir renk seçtikten sonra aşağıdaki **Renkleri Kaydet ve Uygula** butonuna basmalısınız. 

![SS_17.png](img/SS_17.png)

* İhale adının yanındaki renk butonuna basıldığında, kullanılan işletim sistemine ait renk seçici palet görüntülenir. Aşağıda Kubuntu Linux işletim sistemine ait renk paleti görünmektedir. Açık Mor rengi seçilip kayıt tamamlanıyor. 

![SS_18.png](img/SS_18.png)

* Kayıt işlemi sonrası takvim üzerinde İlgili ihalenin rengi mor olarak görüntüleniyor. 

![SS_19.png](img/SS_19.png)
