### Kullanıcı yönetim sistemmi. Girilen verileri JSON ve Pickle formatında kaydedebiliyor.

"""Algoritma:
1. Kullanıcı ekleme (isim,yaş,e-posta)
2. Kullanıcı silme (e-posta)
3. Kullanıcı bilgilerini güncelleme (e-posta)
4. Tüm kullanıcı listeleme"""
import json
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import time
import pickle

# Sayfa yapılandırması
st.set_page_config(
    page_title="Kullanıcı Yönetim Sistemi",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS stil tanımlamaları
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #0D47A1;
        margin-bottom: 1rem;
    }
    .success-msg {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
    }
    .error-msg {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #FFEBEE;
        border-left: 5px solid #F44336;
    }
    .info-card {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0D47A1;
    }
</style>
""", unsafe_allow_html=True)

# Kullanıcı sınıfı - Single Responsibility Principle
class KullaniciYonetimi:
    def __init__(self, dosya_adi="kullanicilar.json", dosya_adi2="kullanicilar.pkl"):
        self.dosya_adi = dosya_adi
        self.dosya_adi2 = dosya_adi2
        self.kullanicilar = self._kullanicilari_yukle()
    
    def _kullanicilari_yukle(self):
        """Kullanıcıları JSON ve Pickle dosyasından yükler"""
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as dosya:
                return json.load(dosya)
        except FileNotFoundError:
            try:
                with open(self.dosya_adi2, "rb") as dosya:
                    return pickle.load(dosya)
            except FileNotFoundError:
                return []
    
    def _kullanicilari_kaydet(self):
        """Kullanıcıları JSON dosyasına kaydeder"""
        with open(self.dosya_adi, "w", encoding="utf-8") as dosya:
            json.dump(self.kullanicilar, dosya, indent=4, ensure_ascii=False)
        """Kullanıcıları Pickle dosyasına kaydeder"""
        with open(self.dosya_adi2, "wb") as dosya:
            pickle.dump(self.kullanicilar, dosya)
            
    
    def kullanici_ekle(self, isim, yas, e_posta):
        """Yeni kullanıcı ekler"""
        # E-posta kontrolü
        for kullanici in self.kullanicilar:
            if kullanici["e_posta"] == e_posta:
                return False, "Bu e-posta adresi zaten kullanılıyor!"
        
        self.kullanicilar.append({"isim": isim, "yas": yas, "e_posta": e_posta})
        self._kullanicilari_kaydet()
        return True, "Kullanıcı başarıyla eklendi!"
    
    def kullanici_sil(self, e_posta):
        """E-posta adresine göre kullanıcı siler"""
        for kullanici in self.kullanicilar:
            if kullanici["e_posta"] == e_posta:
                self.kullanicilar.remove(kullanici)
                self._kullanicilari_kaydet()
                return True, "Kullanıcı başarıyla silindi!"
        return False, "Kullanıcı bulunamadı!"
    
    def kullanici_guncelle(self, e_posta, yeni_isim, yeni_yas):
        """E-posta adresine göre kullanıcı günceller"""
        for kullanici in self.kullanicilar:
            if kullanici["e_posta"] == e_posta:
                kullanici["isim"] = yeni_isim
                kullanici["yas"] = yeni_yas
                self._kullanicilari_kaydet()
                return True, "Kullanıcı başarıyla güncellendi!"
        return False, "Kullanıcı bulunamadı!"
    
    def kullanicilari_getir(self):
        """Tüm kullanıcıları döndürür"""
        return self.kullanicilar

# Kullanıcı yönetim nesnesini oluştur
@st.cache_resource
def kullanici_yonetimi_olustur():
    return KullaniciYonetimi()

kullanici_yonetimi = kullanici_yonetimi_olustur()

# Ana başlık
st.markdown("<h1 class='main-header'>👥 Kullanıcı Yönetim Sistemi</h1>", unsafe_allow_html=True)

# Yan menü
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=300)
    secim = option_menu(
        "Menü",
        ["Ana Sayfa", "Kullanıcı Ekle", "Kullanıcı Sil", "Kullanıcı Güncelle", "Kullanıcıları Listele"],
        icons=["house", "person-plus", "person-x", "pencil-square", "list-ul"],
        menu_icon="cast",
        default_index=0,
    )

# Ana Sayfa
if secim == "Ana Sayfa":
    st.markdown("<h2 class='sub-header'>Hoş Geldiniz!</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h3>Kullanıcı Yönetim Sistemi Nedir?</h3>
            <p>Bu uygulama, kullanıcı bilgilerini yönetmenize yardımcı olan modern bir arayüz sunar.</p>
            <p>Kullanıcı ekleme, silme, güncelleme ve listeleme işlemlerini kolayca yapabilirsiniz.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h3>Nasıl Kullanılır?</h3>
            <p>Sol menüden yapmak istediğiniz işlemi seçin:</p>
            <ul>
                <li>Kullanıcı Ekle: Yeni kullanıcı bilgilerini girin</li>
                <li>Kullanıcı Sil: E-posta adresine göre kullanıcı silin</li>
                <li>Kullanıcı Güncelle: Mevcut kullanıcı bilgilerini güncelleyin</li>
                <li>Kullanıcıları Listele: Tüm kullanıcıları görüntüleyin</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # İstatistikler
    st.markdown("<h3 class='sub-header'>İstatistikler</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Toplam Kullanıcı", len(kullanici_yonetimi.kullanicilari_getir()))
    
    with col2:
        yas_ortalamasi = 0
        if len(kullanici_yonetimi.kullanicilari_getir()) > 0:
            yas_ortalamasi = sum(k["yas"] for k in kullanici_yonetimi.kullanicilari_getir()) / len(kullanici_yonetimi.kullanicilari_getir())
        st.metric("Yaş Ortalaması", f"{yas_ortalamasi:.1f}")
    
    with col3:
        st.metric("Son Güncelleme", "Bugün")

# Kullanıcı Ekle
elif secim == "Kullanıcı Ekle":
    st.markdown("<h2 class='sub-header'>Kullanıcı Ekle</h2>", unsafe_allow_html=True)
    
    with st.form("kullanici_ekle_form"):
        isim = st.text_input("İsim", placeholder="Adınızı girin")
        yas = st.number_input("Yaş", min_value=1, max_value=120, value=25)
        e_posta = st.text_input("E-Posta", placeholder="ornek@mail.com")
        
        submitted = st.form_submit_button("Kullanıcı Ekle")
        
        if submitted:
            if not isim or not e_posta:
                st.markdown("<div class='error-msg'>İsim ve e-posta alanları boş bırakılamaz!</div>", unsafe_allow_html=True)
            else:
                basarili, mesaj = kullanici_yonetimi.kullanici_ekle(isim, yas, e_posta)
                if basarili:
                    st.markdown(f"<div class='success-msg'>{mesaj}</div>", unsafe_allow_html=True)
                    # İşlem başarılı animasyonu
                    with st.spinner("Kullanıcı ekleniyor..."):
                        time.sleep(1)
                    st.balloons()
                else:
                    st.markdown(f"<div class='error-msg'>{mesaj}</div>", unsafe_allow_html=True)

# Kullanıcı Sil
elif secim == "Kullanıcı Sil":
    st.markdown("<h2 class='sub-header'>Kullanıcı Sil</h2>", unsafe_allow_html=True)
    
    # Kullanıcı listesini göster
    kullanicilar = kullanici_yonetimi.kullanicilari_getir()
    if not kullanicilar:
        st.markdown("<div class='info-card'>Henüz kayıtlı kullanıcı bulunmamaktadır.</div>", unsafe_allow_html=True)
    else:
        df = pd.DataFrame(kullanicilar)
        st.dataframe(df, use_container_width=True)
        
        with st.form("kullanici_sil_form"):
            e_posta = st.text_input("Silinecek Kullanıcının E-Posta Adresi", placeholder="ornek@mail.com")
            submitted = st.form_submit_button("Kullanıcıyı Sil")
            
            if submitted:
                if not e_posta:
                    st.markdown("<div class='error-msg'>E-posta alanı boş bırakılamaz!</div>", unsafe_allow_html=True)
                else:
                    basarili, mesaj = kullanici_yonetimi.kullanici_sil(e_posta)
                    if basarili:
                        st.markdown(f"<div class='success-msg'>{mesaj}</div>", unsafe_allow_html=True)
                        with st.spinner("Kullanıcı siliniyor..."):
                            time.sleep(1)
                        st.experimental_rerun()
                    else:
                        st.markdown(f"<div class='error-msg'>{mesaj}</div>", unsafe_allow_html=True)

# Kullanıcı Güncelle
elif secim == "Kullanıcı Güncelle":
    st.markdown("<h2 class='sub-header'>Kullanıcı Güncelle</h2>", unsafe_allow_html=True)
    
    # Kullanıcı listesini göster
    kullanicilar = kullanici_yonetimi.kullanicilari_getir()
    if not kullanicilar:
        st.markdown("<div class='info-card'>Henüz kayıtlı kullanıcı bulunmamaktadır.</div>", unsafe_allow_html=True)
    else:
        df = pd.DataFrame(kullanicilar)
        st.dataframe(df, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            e_posta = st.text_input("Güncellenecek Kullanıcının E-Posta Adresi", placeholder="ornek@mail.com")
            ara_button = st.button("Kullanıcıyı Ara")
        
        if ara_button:
            if not e_posta:
                st.markdown("<div class='error-msg'>E-posta alanı boş bırakılamaz!</div>", unsafe_allow_html=True)
            else:
                kullanici_bulundu = False
                for kullanici in kullanicilar:
                    if kullanici["e_posta"] == e_posta:
                        kullanici_bulundu = True
                        with st.form("kullanici_guncelle_form"):
                            st.markdown("<h3>Kullanıcı Bilgilerini Güncelle</h3>", unsafe_allow_html=True)
                            yeni_isim = st.text_input("Yeni İsim", value=kullanici["isim"])
                            yeni_yas = st.number_input("Yeni Yaş", min_value=1, max_value=120, value=kullanici["yas"])
                            
                            guncelle_button = st.form_submit_button("Güncelle")
                            
                            if guncelle_button:
                                if not yeni_isim:
                                    st.markdown("<div class='error-msg'>İsim alanı boş bırakılamaz!</div>", unsafe_allow_html=True)
                                else:
                                    basarili, mesaj = kullanici_yonetimi.kullanici_guncelle(e_posta, yeni_isim, yeni_yas)
                                    if basarili:
                                        st.markdown(f"<div class='success-msg'>{mesaj}</div>", unsafe_allow_html=True)
                                        with st.spinner("Kullanıcı güncelleniyor..."):
                                            time.sleep(1)
                                        st.experimental_rerun()
                                    else:
                                        st.markdown(f"<div class='error-msg'>{mesaj}</div>", unsafe_allow_html=True)
                        break
                
                if not kullanici_bulundu:
                    st.markdown("<div class='error-msg'>Kullanıcı bulunamadı!</div>", unsafe_allow_html=True)

# Kullanıcıları Listele
elif secim == "Kullanıcıları Listele":
    st.markdown("<h2 class='sub-header'>Kullanıcı Listesi</h2>", unsafe_allow_html=True)
    
    kullanicilar = kullanici_yonetimi.kullanicilari_getir()
    if not kullanicilar:
        st.markdown("<div class='info-card'>Henüz kayıtlı kullanıcı bulunmamaktadır.</div>", unsafe_allow_html=True)
    else:
        # Arama filtresi
        arama = st.text_input("E-Postaya Göre Ara", placeholder="Arama yapmak için e-posta girin...")
        
        # Filtreleme
        if arama:
            filtrelenmis_kullanicilar = [k for k in kullanicilar if arama.lower() in k["e_posta"].lower()]
        else:
            filtrelenmis_kullanicilar = kullanicilar
        
        # DataFrame oluştur
        df = pd.DataFrame(filtrelenmis_kullanicilar)
        
        # Sıralama seçenekleri
        siralama = st.selectbox("Sıralama", ["İsim (A-Z)", "İsim (Z-A)", "Yaş (Küçükten Büyüğe)", "Yaş (Büyükten Küçüğe)"])
        
        if siralama == "İsim (A-Z)":
            df = df.sort_values(by="isim")
        elif siralama == "İsim (Z-A)":
            df = df.sort_values(by="isim", ascending=False)
        elif siralama == "Yaş (Küçükten Büyüğe)":
            df = df.sort_values(by="yas")
        elif siralama == "Yaş (Büyükten Küçüğe)":
            df = df.sort_values(by="yas", ascending=False)
        
        # Tabloyu göster
        st.dataframe(df, use_container_width=True)
        
        # İstatistikler
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Toplam Kullanıcı", len(kullanicilar))
        
        with col2:
            yas_ortalamasi = sum(k["yas"] for k in kullanicilar) / len(kullanicilar) if kullanicilar else 0
            st.metric("Yaş Ortalaması", f"{yas_ortalamasi:.1f}")
        
        with col3:
            en_genc = min(kullanicilar, key=lambda x: x["yas"])["yas"] if kullanicilar else "-"
            en_yasli = max(kullanicilar, key=lambda x: x["yas"])["yas"] if kullanicilar else "-"
            st.metric("Yaş Aralığı", f"{en_genc} - {en_yasli}")
        
        # Grafik gösterimi
        st.markdown("<h3>Yaş Dağılımı</h3>", unsafe_allow_html=True)
        
        # Yaş grupları oluştur
        yas_gruplari = {
            "0-18": 0,
            "19-30": 0,
            "31-45": 0,
            "46-60": 0,
            "60+": 0
        }
        
        for kullanici in kullanicilar:
            yas = kullanici["yas"]
            if yas <= 18:
                yas_gruplari["0-18"] += 1
            elif yas <= 30:
                yas_gruplari["19-30"] += 1
            elif yas <= 45:
                yas_gruplari["31-45"] += 1
            elif yas <= 60:
                yas_gruplari["46-60"] += 1
            else:
                yas_gruplari["60+"] += 1
        
        # Grafik çiz
        st.bar_chart(yas_gruplari)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 1rem; background-color: #F5F5F5; border-radius: 0.5rem;">
    <p>© 2025 Kullanıcı Yönetim Sistemi | Streamlit ile geliştirilmiştir</p>
</div>
""", unsafe_allow_html=True)