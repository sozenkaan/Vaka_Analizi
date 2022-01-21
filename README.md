# Vaka_Analizi

Bu çalışmada 2 adet sorunun vaka analizi yapılmıştır.
Soru 1:  
Gerekli kodlar,alan ve zaman karmaşıklığı açıklama satırları içerisinde anlatılmaktadır.
Soru 2:
Burada hospital.csv verisetinin analizi yapılacaktır.
Burada denetimsiz öğrenme uygulayamayız.Çünkü string formatında veriler yer almakta olup bu veriler içerisinde çok sayıda nitelik yer aldığından dolayı one_hot_encoder uygulanamadığından veriler vektöre dönüştürülemeyecektir ve denetimsiz öğrenme uygulanamaz.
Uygulanacak adımlar şu şekildedir:
1- hospital.csv veriseti yüklenir. 
2-Verisetinde eksik ve tutarsız değer var olup olmadığı analizi yapılır(nan type).
3-Veri setinde eksik ve tutarsız veri yok ise verisetinde yer alan sütunlar incelenir.Verisetinde yer alan sütunlarda string veri yer alıyorsa burada one-hot-encoder işlemi uygulanır ve belirtilen sütunlar vektöre dönüştürülmüş olur.Verisetinde yer alan sütunlarda categorical veri yer alıyorsa burada label-encoder işlemi uygulanır ve belirtilen sütunlar binary(0,1) formuna dönüştürülür.
4- Verisetinde yer alan değişkenler concat fonksiyonu aracılığı ile tekrar bir dataframe olarak birleştirilir.
5- Veriler train test split metodu ile eğitim ve test verisi olarak bölünür.Veriler üzerinde çok nitelik bulunmasaydı, rnn veya lstm  uygulanarak model eğitimi gerçekleştirilip,model üzerinde prediction işlemi gerçekleştirilebilirdi.Rnn ve lstm mimarilerini tercih etmemin nedeni ise metinsel verilerde yüksek doğruluk elde edilebiliyor olmamız.

Yine de soru2 yi pratik olarak python üzerinde uygulamaya çalıştım.Soru 2 de burada case_study2.py dosyası olarak yer alıyor.
