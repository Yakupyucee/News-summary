import requests
from bs4 import BeautifulSoup

# Örnek bir haber sayfası URL'si
sayfa_url = "https://www.trthaber.com/"

def haber_url_listesi_getir(site_url):
    try:
        # URL'yi get isteğiyle çekme
        response = requests.get(site_url)
        response.raise_for_status()  # İstek başarısız olursa hata fırlat
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Tüm haberlerin bulunduğu div'i seçme
        haberler_div = soup.find_all("div", class_="standard-card")
        
        # Haber URL'lerini depolamak için boş bir liste oluşturma
        haber_url_listesi = []
        
        # Her bir haber div'ini dolaşma
        for haber_div in haberler_div:
            # Her bir haber div'indeki URL'yi bulma
            haber_url = haber_div.find("a", class_="site-url")["href"]
            haber_url_listesi.append(haber_url)
        
        return haber_url_listesi
        
    except Exception as e:
        print("Hata:", e)
        return []

def haber_basligi_cek(url):
    try:
        # Web sayfasını getir
        response = requests.get(url)
        # HTML içeriğini analiz etmek için BeautifulSoup kullanarak parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Haber başlığını içeren h1'i bul
        news_title_h1 = soup.find('h1', class_='news-title')

        if news_title_h1:
            haber_basligi = news_title_h1.get_text().strip()
            return haber_basligi
        else:
            print("Haber başlığı bulunamadı.")
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def haber_kaynagi_cek(url):
    try:
        # Web sayfasını getir
        response = requests.get(url)
        # HTML içeriğini analiz etmek için BeautifulSoup kullanarak parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Haber kaynağını içeren span'i bul
        source_span = soup.find('span', class_='source')

        if source_span:
            # Kaynak bilgisini bul ve temizle
            label = source_span.find('label')
            if label:
                label.decompose()  # <label>KAYNAK</label> etiketini kaldır
            haber_kaynagi = source_span.get_text().strip()
            return haber_kaynagi
        else:
            print("Haber kaynağı bulunamadı.")
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def haber_tarihi_cek(url):
    try:
        # Web sayfasını getir
        response = requests.get(url)
        # HTML içeriğini analiz etmek için BeautifulSoup kullanarak parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Haber tarihini içeren time etiketini bul
        time_tag = soup.find('time', class_='updated-date-content')

        if time_tag:
            # Datetime attribute'ündeki bilgiyi al
            haber_tarihi = time_tag['datetime']
            return haber_tarihi
        else:
            print("Haber tarihi bulunamadı.")
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def resim_url_cek(url):
    try:
        # Web sayfasını getir
        response = requests.get(url)
        # HTML içeriğini analiz etmek için BeautifulSoup kullanarak parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Resim URL'sini içeren picture etiketini ve source etiketini bul
        picture_tag = soup.find('picture')
        if picture_tag:
            source_tag = picture_tag.find('source')
            if source_tag:
                # data-srcset attribute'ündeki bilgiyi al
                resim_url = source_tag['data-srcset']
                # URL'den gereksiz boşlukları temizle
                resim_url = resim_url.strip()
                return resim_url
            else:
                print("Resim URL'si bulunamadı.")
                return None
        else:
            print("Resim URL'si bulunamadı.")
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def haber_spot_cek(url):
    try:
        # Web sayfasını getir
        response = requests.get(url)
        # HTML içeriğini analiz etmek için BeautifulSoup kullanarak parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Haber spotunu içeren h2'i bul
        news_spot_h2 = soup.find('h2', class_='news-spot')

        if news_spot_h2:
            haber_spot = news_spot_h2.get_text().strip()
            return haber_spot
        else:
            print("Haber spotu bulunamadı.")
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def haber_metni_cek(url):
    try:
        # Web sayfasını getir
        response = requests.get(url)
        # HTML içeriğini analiz etmek için BeautifulSoup kullanarak parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Haber metnini içeren div'i bul
        news_content_div = soup.find('div', class_='news-content')

        if news_content_div:
            haber_metni = news_content_div.get_text().strip()
            return haber_metni
        else:
            print("Haber metni bulunamadı.")
            return None
    except Exception as e:
        print("Hata:", e)
        return None

def get_and_remove_next_element(lst):
    if not lst:
        return "N"
    next_element = lst.pop(0)
    return next_element

html_template = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}

        .element {{
            margin-bottom: 20px;
            border: 2px solid #000;
            padding: 10px;
        }}

        .title {{
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 10px;
            text-decoration: none;
            color: black;

        }}

        .source {{
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
        }}

        .image-container {{
            position: relative;
            padding-bottom: 56.25%;
            padding-top: 30px;
            height: 0;
            overflow: hidden;
            border: 2px solid #000;
        }}

        .image {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .spot {{
            font-size: 19px;
            background-color: #666;
            color: #fff;
            padding: 5px 10px;
            position: absolute;
            bottom: 10px;
            left: 10px;
            border-radius: 5px;
            border: 2px solid #000;
        }}

        .date {{
            font-size: 14px;
            color: #666;
            margin-top: 10px;
        }}
    </style>
    <title>Basic Screen Layout</title>
</head>
<body>
    {content}
</body>
</html>
"""





def main():
    global sayfa_url
    sayac = 1
    haber_url_listesi = haber_url_listesi_getir(sayfa_url)
    
    haber_sayisi = len(haber_url_listesi)
    print(haber_sayisi, "tane haber var.")

    html_content = ""

    while sayac <= 15:
        if not haber_url_listesi:
            print('-----HABERLERİN SONU-----')
            break
        haber_url = get_and_remove_next_element(haber_url_listesi)
        print(sayac, ". Haber")
        sayac += 1

        haber_metni = haber_metni_cek(haber_url)
        if not haber_metni:
            print("Haber metni çekilemedi.")
            sayac -= 1
            continue
        
        haber_basligi = haber_basligi_cek(haber_url)
        if not haber_basligi:
            haber_basligi = "Başlık bulunamadı"

        haber_spot = haber_spot_cek(haber_url)
        if not haber_spot:
            haber_spot = "Spot bulunamadı"

        haber_kaynagi = haber_kaynagi_cek(haber_url)
        if not haber_kaynagi:
            haber_kaynagi = "Kaynak bulunamadı"

        haber_tarihi = haber_tarihi_cek(haber_url)
        if not haber_tarihi:
            haber_tarihi = "Tarih bulunamadı"

        resim_url = resim_url_cek(haber_url)
        if not resim_url:
            resim_url = "Resim bulunamadı"

        # Haber HTML içeriği oluşturma
        html_content += f"""
        <div class="element">
            <div class="source">{haber_kaynagi}</div>
            <div class="image-container">
                <img class="image" src="{resim_url}" alt="Image description">
                <div class="spot">{haber_spot}</div>
            </div>
            <div class="title"><a href="{haber_url}" target="_blank">{haber_basligi}</a></div>
            <div class="date">{haber_tarihi}</div>
        </div>
        """
    



  
    # Tüm içeriği şablona ekle
    final_html = html_template.format(content=html_content)
    
    # HTML dosyasına yazma işlemi
    try:
        with open("C:\\Users\\YAKUP\\Desktop\\Project\\index.html", "w", encoding="utf-8") as file:
            file.write(final_html)
        print("HTML dosyası başarıyla oluşturuldu.")
    except Exception as e:
        print("HTML dosyası oluşturulamadı:", e)


if __name__ == "__main__":
    
    main()

