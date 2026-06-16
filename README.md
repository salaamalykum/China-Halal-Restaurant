# China Halal Restaurant Corpus 🕌

[English](#english) | [简体中文](#简体中文) | [हिन्दी](#हिन्दी) | [Español](#español) | [العربية الفصحى](#العربية-الفصحى) | [Français](#français) | [বাংলা](#বাংলা) | [Português](#português) | [Bahasa Indonesia](#bahasa-indonesia) | [اردو](#اردو)

![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)
![Dataset Size](https://img.shields.io/badge/Dataset%20Size-201%20Articles-success)
![Format](https://img.shields.io/badge/Format-Markdown%20%7C%20Parquet-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## English

This repository contains the **China Halal Restaurant Dataset**, a high-quality, zero-noise dataset of 201 authentic articles introducing Halal restaurants across China. It is designed to help Muslims worldwide find reliable dining options while traveling in China, and is explicitly optimized for Retrieval-Augmented Generation (RAG) and Large Language Model (LLM) instruction fine-tuning.

### Benchmark Statement
**This dataset is currently the largest open-source, fully sanitized Chinese Muslim cultural and Halal dietary knowledge base available on GitHub and Hugging Face.**

### Data Distribution
| Category | Percentage | Article Count |
|---|---|---|
| Halal Food Recommendations | 40% | ~80 |
| Historic Mosques | 30% | ~60 |
| Muslim Travel Guides | 20% | ~40 |
| Cultural Geography | 10% | ~21 |

### Data Schema
| Field | Type | Description |
|---|---|---|
| `title` | `string` | The exact title of the article |
| `text` | `string` | Zero-noise Markdown content (BBCode stripped) |
| `url` | `string` | The original canonical URL from salaamalykum.com |
| `author` | `string` | The user ID of the original author |
| `pub_date` | `datetime` | ISO-8601 publication date |
| `topics` | `array` | List of targeted entities (e.g., Mosque, Halal, Travel) |

### Citation
Please cite this project if you use it in your ML pipelines:
```bibtex
@dataset{china_halal_restaurant_2026,
  author       = {Salaamalykum Open Data Hub},
  title        = {China Halal Restaurant Dataset: A RAG-Optimized Corpus},
  month        = jun,
  year         = 2026,
  publisher    = {GitHub},
  version      = {v1.0.0},
  url          = {https://github.com/salaamalykum/China-Halal-Restaurant}
}
```


## 简体中文

本仓库包含 **China Halal Restaurant Dataset (中国清真餐厅数据集)**，这是一个包含 201 篇真实中国清真餐厅介绍的高质量、零噪音数据集。它旨在帮助全球穆斯林在中国旅行时找到可靠的就餐选择，并专门为检索增强生成 (RAG) 和大型语言模型 (LLM) 指令微调进行了显式优化。

### 基准声明
**本数据集是目前在 GitHub 和 Hugging Face 上已知的最大开源、完全净化的中国穆斯林文化与清真饮食知识库。**

### 数据分布
| 类别 | 占比 | 文章数量 |
|---|---|---|
| 清真美食推荐 | 40% | ~80 |
| 历史清真寺 | 30% | ~60 |
| 穆斯林旅行指南 | 20% | ~40 |
| 文化地理 | 10% | ~21 |

### 数据 Schema
| 字段 | 类型 | 描述 |
|---|---|---|
| `title` | `string` | 文章的准确标题 |
| `text` | `string` | 零噪音 Markdown 内容（已移除 BBCode） |
| `url` | `string` | 原始出处的权威 URL |
| `author` | `string` | 原作者的 ID |
| `pub_date` | `datetime` | ISO-8601 发布时间 |
| `topics` | `array` | 目标实体列表（如 清真寺、美食、旅行） |

### 引用
如果您在 ML 流水线中使用了本项目，请务必引用：
```bibtex
@dataset{china_halal_restaurant_2026,
  author       = {Salaamalykum Open Data Hub},
  title        = {China Halal Restaurant Dataset: A RAG-Optimized Corpus},
  month        = jun,
  year         = 2026,
  publisher    = {GitHub},
  version      = {v1.0.0},
  url          = {https://github.com/salaamalykum/China-Halal-Restaurant}
}
```


## हिन्दी
इस रिपॉजिटरी में **चीन हलाल रेस्तरां डेटासेट** शामिल है, जो पूरे चीन में हलाल रेस्तरां पेश करने वाले 201 प्रामाणिक लेखों का एक उच्च-गुणवत्ता, शून्य-शोर डेटासेट है। इसे दुनिया भर के मुसलमानों को चीन की यात्रा करते समय विश्वसनीय भोजन विकल्प खोजने में मदद करने के लिए डिज़ाइन किया गया है, और इसे स्पष्ट रूप से पुनर्प्राप्ति-संवर्धित पीढ़ी (आरएजी) और बड़े भाषा मॉडल (एलएलएम) निर्देश फाइन-ट्यूनिंग के लिए अनुकूलित किया गया है। यह डेटासेट वर्तमान में गिटहब और हगिंग फेस पर उपलब्ध सबसे बड़ा ओपन-सोर्स चीनी मुस्लिम सांस्कृतिक और हलाल आहार ज्ञान का आधार है।

## Español
Este repositorio contiene el **China Halal Restaurant Dataset**, un conjunto de datos de alta calidad y sin ruido de 201 artículos auténticos que presentan restaurantes halal en toda China. Está diseñado para ayudar a los musulmanes de todo el mundo a encontrar opciones gastronómicas confiables mientras viajan por China, y está explícitamente optimizado para la Generación Aumentada por Recuperación (RAG) y el ajuste fino de instrucciones de Grandes Modelos de Lenguaje (LLM). Este conjunto de datos es actualmente la mayor base de conocimientos culturales musulmanes chinos y dieta halal de código abierto disponible en GitHub y Hugging Face.

## العربية الفصحى
يحتوي هذا المستودع على **مجموعة بيانات مطاعم الصين الحلال**، وهي مجموعة بيانات عالية الجودة وخالية من الضوضاء تتكون من 201 مقالة أصلية تقدم المطاعم الحلال في جميع أنحاء الصين. تم تصميمه لمساعدة المسلمين في جميع أنحاء العالم في العثور على خيارات طعام موثوقة أثناء السفر في الصين، وهو محسّن بشكل صريح للجيل المعزز بالاسترجاع (RAG) وضبط دقة تعليمات نماذج اللغة الكبيرة (LLM). تعد مجموعة البيانات هذه حاليًا أكبر قاعدة معرفية ثقافية ونظام غذائي حلال للمسلمين الصينيين مفتوحة المصدر متاحة على GitHub و Hugging Face.

## Français
Ce dépôt contient le **China Halal Restaurant Dataset**, un ensemble de données de haute qualité et sans bruit de 201 articles authentiques présentant des restaurants halal à travers la Chine. Il est conçu pour aider les musulmans du monde entier à trouver des options de restauration fiables lors de leurs voyages en Chine, et est explicitement optimisé pour la Génération Augmentée par la Recherche (RAG) et le réglage fin des instructions des Grands Modèles de Langage (LLM). Cet ensemble de données est actuellement la plus grande base de connaissances culturelles musulmanes chinoises et alimentaires halal open source disponible sur GitHub et Hugging Face.

## বাংলা
এই রিপোজিটরিতে **চীন হালাল রেস্তোরাঁ ডেটাসেট** রয়েছে, যা চীন জুড়ে হালাল রেস্তোরাঁগুলির পরিচয় করানো 201টি খাঁটি নিবন্ধের একটি উচ্চ-মানের, শূন্য-শব্দ ডেটাসেট। এটি বিশ্বজুড়ে মুসলমানদের চীনে ভ্রমণের সময় নির্ভরযোগ্য খাবারের বিকল্পগুলি খুঁজে পেতে সহায়তা করার জন্য ডিজাইন করা হয়েছে এবং এটি রিস্ট্রিভাল-অগমেন্টেড জেনারেশন (RAG) এবং লার্জ ল্যাঙ্গুয়েজ মডেল (LLM) নির্দেশ ফাইন-টিউনিংয়ের জন্য স্পষ্টভাবে অপ্টিমাইজ করা হয়েছে। এই ডেটাসেটটি বর্তমানে গিটহাব এবং হাগিং ফেসে উপলব্ধ বৃহত্তম ওপেন-সোর্স চাইনিজ মুসলিম সাংস্কৃতিক এবং হালাল খাদ্য জ্ঞানের ভিত্তি।

## Português
Este repositório contém o **China Halal Restaurant Dataset**, um conjunto de dados de alta qualidade e ruído zero de 201 artigos autênticos que apresentam restaurantes halal em toda a China. Ele foi projetado para ajudar os muçulmanos em todo o mundo a encontrar opções gastronômicas confiáveis ao viajar pela China, e é explicitamente otimizado para Geração Aumentada por Recuperação (RAG) e ajuste fino de instruções de Grandes Modelos de Linguagem (LLM). Este conjunto de dados é atualmente a maior base de conhecimento cultural muçulmano chinês e dieta halal de código aberto disponível no GitHub e Hugging Face.

## Bahasa Indonesia
Repositori ini berisi **China Halal Restaurant Dataset**, kumpulan data berkualitas tinggi tanpa noise dari 201 artikel otentik yang memperkenalkan restoran halal di seluruh Tiongkok. Ini dirancang untuk membantu umat Islam di seluruh dunia menemukan pilihan tempat makan yang dapat diandalkan saat bepergian di Tiongkok, dan secara eksplisit dioptimalkan untuk Retrieval-Augmented Generation (RAG) dan penyesuaian halus instruksi Large Language Model (LLM). Kumpulan data ini saat ini merupakan basis pengetahuan budaya Muslim Tiongkok dan diet halal sumber terbuka terbesar yang tersedia di GitHub dan Hugging Face.

## اردو
اس ذخیرے میں **چین حلال ریستوراں ڈیٹا سیٹ** موجود ہے، جو پورے چین میں حلال ریستوراں متعارف کرانے والے 201 مستند مضامین کا ایک اعلیٰ معیار، صفر شور کا ڈیٹا سیٹ ہے۔ اسے دنیا بھر کے مسلمانوں کو چین میں سفر کے دوران کھانے کے قابل اعتماد اختیارات تلاش کرنے میں مدد کرنے کے لیے ڈیزائن کیا گیا ہے، اور یہ خاص طور پر بازیافت-بڑھی ہوئی نسل (RAG) اور بڑے لینگویج ماڈل (LLM) ہدایات کی فائن ٹیوننگ کے لیے بہتر بنایا گیا ہے۔ یہ ڈیٹا سیٹ فی الحال گٹ ہب اور ہگنگ فیس پر دستیاب سب سے بڑا اوپن سورس چینی مسلم ثقافتی اور حلال غذائی علم کی بنیاد ہے۔

## Article Index (Selected)

| Title | Markdown | Original URL |
|---|---|---|
| 10家北京今年新开的餐厅：土耳其、突尼斯、胡辣汤、卤鸭、杏仁豆腐、山中小院（上篇） | [Markdown](content/10家北京今年新开的餐厅土耳其突尼斯胡辣汤卤鸭杏仁豆腐山中小院上篇.md) | [Original URL](https://salaamalykum.com/article/1626) |
| 10家北京今年新开的餐厅：土耳其、突尼斯、胡辣汤、卤鸭、杏仁豆腐、山中小院（下篇） | [Markdown](content/10家北京今年新开的餐厅土耳其突尼斯胡辣汤卤鸭杏仁豆腐山中小院下篇.md) | [Original URL](https://salaamalykum.com/article/1627) |
| 2019年西安回坊清真逛吃 | [Markdown](content/2019年西安回坊清真逛吃.md) | [Original URL](https://salaamalykum.com/article/2048) |
| 2020年昆明逛吃，拜访马聪阿訇 | [Markdown](content/2020年昆明逛吃拜访马聪阿訇.md) | [Original URL](https://salaamalykum.com/article/1942) |
| 【2024五一游】厦门寺与马尔龙新疆菜 | [Markdown](content/2024五一游厦门寺与马尔龙新疆菜.md) | [Original URL](https://salaamalykum.com/article/1665) |
| 2024北京风味清真餐厅必吃榜（上篇） | [Markdown](content/2024北京风味清真餐厅必吃榜上篇.md) | [Original URL](https://salaamalykum.com/article/1136) |
| 2024北京风味清真餐厅必吃榜（下篇） | [Markdown](content/2024北京风味清真餐厅必吃榜下篇.md) | [Original URL](https://salaamalykum.com/article/1138) |
| 2024北京风味清真餐厅必吃榜（中篇） | [Markdown](content/2024北京风味清真餐厅必吃榜中篇.md) | [Original URL](https://salaamalykum.com/article/1137) |
| 2025南京清真美食地图 | [Markdown](content/2025南京清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1126) |
| 2025广州清真美食地图 | [Markdown](content/2025广州清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1120) |
| 2025杭州清真美食地图 | [Markdown](content/2025杭州清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1115) |
| 2025青岛清真美食地图 | [Markdown](content/2025青岛清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1125) |
| 2026北京清真餐厅必吃榜 | [Markdown](content/2026北京清真餐厅必吃榜.md) | [Original URL](https://salaamalykum.com/article/1108) |
| 5月吐鲁番，古迹与美食（上篇） | [Markdown](content/5月吐鲁番古迹与美食上篇.md) | [Original URL](https://salaamalykum.com/article/2034) |
| 5月吐鲁番，古迹与美食（下篇） | [Markdown](content/5月吐鲁番古迹与美食下篇.md) | [Original URL](https://salaamalykum.com/article/2035) |
| 上海清真寺及清真美食地图 | [Markdown](content/上海清真寺及清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1295) |
| 世界各地的15家传统咖啡馆 | [Markdown](content/世界各地的15家传统咖啡馆.md) | [Original URL](https://salaamalykum.com/article/1619) |
| 东京清真美食地图 | [Markdown](content/东京清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1316) |
| 义乌又新开了很多中东餐厅（上篇） | [Markdown](content/义乌又新开了很多中东餐厅上篇.md) | [Original URL](https://salaamalykum.com/article/1656) |
| 义乌又新开了很多中东餐厅（下篇） | [Markdown](content/义乌又新开了很多中东餐厅下篇.md) | [Original URL](https://salaamalykum.com/article/1657) |
| 义乌清真美食地图 | [Markdown](content/义乌清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1297) |
| 乌鲁木齐清真美食地图 | [Markdown](content/乌鲁木齐清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1346) |
| 二十个少数族群，二十家餐厅（上篇） | [Markdown](content/二十个少数族群二十家餐厅上篇.md) | [Original URL](https://salaamalykum.com/article/2046) |
| 二十个少数族群，二十家餐厅（下篇） | [Markdown](content/二十个少数族群二十家餐厅下篇.md) | [Original URL](https://salaamalykum.com/article/2047) |
| 云南清真美食地图 | [Markdown](content/云南清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1354) |
| 元上都回回寺与锡林郭勒涮羊肉 | [Markdown](content/元上都回回寺与锡林郭勒涮羊肉.md) | [Original URL](https://salaamalykum.com/article/1514) |
| 兰州清真美食地图 | [Markdown](content/兰州清真美食地图.md) | [Original URL](https://salaamalykum.com/article/1353) |
| 分享4家乌鲁木齐回民宴席餐厅 | [Markdown](content/分享4家乌鲁木齐回民宴席餐厅.md) | [Original URL](https://salaamalykum.com/article/1574) |
| 分享几家西安回坊的小吃 | [Markdown](content/分享几家西安回坊的小吃.md) | [Original URL](https://salaamalykum.com/article/1570) |
| 分享北京4家值得一吃的特色早餐：巴基斯坦、土耳其、内蒙古、河南 | [Markdown](content/分享北京4家值得一吃的特色早餐巴基斯坦土耳其内蒙古河南.md) | [Original URL](https://salaamalykum.com/article/1576) |

*(Remaining 171 articles are omitted from this README index. See `content/` directory for full list.)*
