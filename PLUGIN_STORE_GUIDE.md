# FlowLauncher Plugin Store'a Ekleme Rehberi

Bu rehber, Tureng Dictionary eklentisini FlowLauncher Plugin Store'a eklemek için gerekli adımları açıklar.

## Ön Hazırlık

### 1. GitHub Repository Kontrolü

✅ Repository adı: `FlowLauncher.Tureng.Dictionary`  
✅ Repository URL: `https://github.com/vlamz/FlowLauncher.Tureng.Dictionary`  
✅ Tüm dosyalar yüklendi mi?  
✅ README.md güncel mi?  
✅ LICENSE dosyası var mı? (GPL-3.0 olarak görünüyor)

### 2. Release Oluşturma

1. GitHub repository'nizde **Releases** sekmesine gidin
2. **"Create a new release"** butonuna tıklayın
3. **Tag version**: `1.0.0` (veya `v1.0.0`)
4. **Release title**: `Tureng Dictionary-1.0.0`
5. **Description**: Release notlarınızı ekleyin
6. **Release dosyası hazırlama**:
   - `TurengPlugin` klasörünün içindeki tüm dosyaları ZIP olarak sıkıştırın
   - ZIP dosyasının adı: `Tureng Dictionary-1.0.0.zip` olmalı
   - ZIP içinde şunlar olmalı:
     - `main.py`
     - `plugin.json`
     - `SettingsTemplate.yaml`
     - `README.md`
     - `images/tureng.png`
     - `plugin/` klasörü (Tureng.py ve __init__.py)
     - `lib/flowlauncher/` klasörü (tüm FlowLauncher kütüphanesi)
7. ZIP dosyasını release'e ekleyin
8. **"Publish release"** butonuna tıklayın

## FlowLauncher Plugin Store'a Ekleme

### Adım 1: FlowLauncher PluginsManifest Repository'sini Fork Edin

1. [Flow.Launcher.PluginsManifest](https://github.com/Flow-Launcher/Flow.Launcher.PluginsManifest) repository'sine gidin
2. Sağ üstteki **"Fork"** butonuna tıklayın
3. Fork'u kendi hesabınıza oluşturun

### Adım 2: Plugin JSON Dosyası Oluşturun

1. Fork'ladığınız repository'de `plugins` klasörüne gidin
2. Yeni bir JSON dosyası oluşturun
3. Dosya adı formatı: `Tureng Dictionary-{UUID}.json`
   - UUID için benzersiz bir ID kullanın (örnek: `a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d`)

### Adım 3: JSON İçeriğini Hazırlayın

Aşağıdaki JSON formatını kullanın:

```json
{
  "ID": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
  "ActionKeyword": "tureng",
  "Name": "Tureng Dictionary",
  "Description": "An unofficial FlowLauncher plugin to easily access Tureng Dictionary.",
  "Author": "Vlamz",
  "Version": "1.0.0",
  "Language": "python",
  "Website": "https://github.com/vlamz/FlowLauncher.Tureng.Dictionary",
  "IcoPath": "images\\tureng.png",
  "ExecuteFileName": "main.py",
  "DownloadLink": "https://github.com/vlamz/FlowLauncher.Tureng.Dictionary/releases/download/1.0.0/Tureng.Dictionary-1.0.0.zip"
}
```

**Önemli Notlar:**
- `DownloadLink`: GitHub release'inizdeki ZIP dosyasının direkt linki olmalı
- Link formatı: `https://github.com/{username}/{repo}/releases/download/{tag}/{filename}.zip`
- Release oluşturduktan sonra ZIP dosyasına sağ tıklayıp "Copy link address" ile linki alabilirsiniz

### Adım 4: Pull Request Oluşturun

1. Fork'ladığınız repository'de değişikliklerinizi commit edin
2. **"Create Pull Request"** butonuna tıklayın
3. PR başlığı: `Add Tureng Dictionary plugin`
4. PR açıklaması:
   ```
   ## Plugin Information
   - Name: Tureng Dictionary
   - Author: Vlamz
   - Version: 1.0.0
   - Description: An unofficial FlowLauncher plugin to easily access Tureng Dictionary.
   - Repository: https://github.com/vlamz/FlowLauncher.Tureng.Dictionary
   - Action Keyword: tureng
   
   ## Features
   - Multi-language support (Turkish-English, French-English, Spanish-English, German-English)
   - Default language settings
   - Context menu with alternative language options
   - Secure URL generation and error handling
   ```
5. PR'yi gönderin

### Adım 5: Onay Bekleme

- FlowLauncher ekibi PR'nizi inceleyecek
- Gerekirse geri bildirim verebilirler
- Onaylandıktan sonra eklentiniz Plugin Store'da görünecek

## Kontrol Listesi

- [ ] GitHub repository oluşturuldu
- [ ] Tüm dosyalar yüklendi
- [ ] Release oluşturuldu (Tureng Dictionary-1.0.0)
- [ ] ZIP dosyası release'e eklendi
- [ ] PluginsManifest repository fork'landı
- [ ] Plugin JSON dosyası oluşturuldu
- [ ] DownloadLink doğru formatta
- [ ] Pull Request oluşturuldu
- [ ] PR açıklaması dolduruldu

## İpuçları

1. **UUID Oluşturma**: Online UUID generator kullanabilirsiniz (örnek: https://www.uuidgenerator.net/)
2. **Download Link**: Release oluşturduktan sonra ZIP dosyasının linkini alın
3. **Test**: Release ZIP'ini indirip FlowLauncher'da test edin
4. **README**: README.md dosyanızın güncel olduğundan emin olun

## Yardım

Sorun yaşarsanız:
- FlowLauncher Discord sunucusuna katılın
- GitHub Issues'da soru sorun
- Mevcut plugin örneklerini inceleyin

