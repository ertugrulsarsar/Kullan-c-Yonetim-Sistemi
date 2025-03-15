# Kullanıcı Yönetim Sistemi

Bu proje, kullanıcı bilgilerini yönetmenize yardımcı olan bir uygulamadır. Kullanıcı ekleme, silme, güncelleme ve listeleme işlemlerini kolayca yapabilirsiniz. Uygulama, kullanıcı verilerini JSON ve Pickle formatında kaydedebilir.

## Özellikler

- Kullanıcı ekleme (isim, yaş, e-posta)
- Kullanıcı silme (e-posta)
- Kullanıcı bilgilerini güncelleme (e-posta)
- Tüm kullanıcıları listeleme
- Kullanıcı verilerini JSON ve Pickle formatında kaydetme

## Kurulum

1. Bu projeyi klonlayın veya indirin.

## Kullanım

1. Uygulamayı başlatmak için aşağıdaki komutu çalıştırın:

    ```sh
    streamlit run main.py
    ```

2. Tarayıcınızda açılan sayfada, sol menüden yapmak istediğiniz işlemi seçin:
    - **Ana Sayfa**: Uygulama hakkında bilgi ve istatistikler.
    - **Kullanıcı Ekle**: Yeni kullanıcı bilgilerini girin.
    - **Kullanıcı Sil**: E-posta adresine göre kullanıcı silin.
    - **Kullanıcı Güncelle**: Mevcut kullanıcı bilgilerini güncelleyin.
    - **Kullanıcıları Listele**: Tüm kullanıcıları görüntüleyin.

## Dosya Yapısı

- `main.py`: Uygulamanın ana dosyası.
- `kullanicilar.json`: Kullanıcı verilerinin JSON formatında saklandığı dosya.
- `kullanicilar.pkl`: Kullanıcı verilerinin Pickle formatında saklandığı dosya.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
