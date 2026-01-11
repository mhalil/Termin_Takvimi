import pandas as pd
import json

def xlsx_to_js(excel_dosyasi, cikis_js_dosyasi="veriler.js"):
    try:
        # Excel dosyasını oku
        df = pd.read_excel(excel_dosyasi)
        
        # Sütun isimlerindeki boşlukları temizle
        df.columns = [c.strip() for c in df.columns]
        
        # 1. Tarih Düzenlemesi
        tarih_sutunu = 'Parti Son Teslim Tarihi'
        if tarih_sutunu in df.columns:
            df[tarih_sutunu] = pd.to_datetime(df[tarih_sutunu]).dt.strftime('%Y-%m-%d')
        
        # 2. Sayı Formatı Düzenlemesi (Noktayı Virgüle Çevirme)
        # 'Parti Tutarı' sütunundaki sayıları metne çevirip virgüllü hale getirir
        tutar_sutunu = 'Parti Tutarı'
        if tutar_sutunu in df.columns:
            # Sayıyı 10250000.0 -> "10250000,00" formatına sokar
            # Binlik ayırıcı istemiyorsanız sadece replace('.', ',') yeterlidir.
            df[tutar_sutunu] = df[tutar_sutunu].apply(lambda x: f"{x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') if pd.notnull(x) else x)
            # Not: Üstteki satır hem binlik ayırıcıyı nokta yapar, hem ondalığı virgül.
            # Eğer sadece ondalık virgül olsun, binlik ayırıcı olmasın derseniz:
            # df[tutar_sutunu] = df[tutar_sutunu].apply(lambda x: str(x).replace('.', ',') if pd.notnull(x) else x)

        # Veriyi liste formatına çevir
        data_list = df.to_dict(orient='records')
        
        # JS içeriğini oluştur
        js_content = f"const ihaleVerileri = {json.dumps(data_list, ensure_ascii=False, indent=4)};"
        
        with open(cikis_js_dosyasi, "w", encoding="utf-8") as f:
            f.write(js_content)
            
        print(f"✅ Başarılı! '{cikis_js_dosyasi}' oluşturuldu (Virgül ayracı uygulandı).")
        
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")

# Excel dosyanızın adını buraya yazın
xlsx_to_js("Termin bilgileri.xlsx")
