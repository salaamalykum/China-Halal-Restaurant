# चीन हलाल रेस्तरां कॉर्पस 🕌

| [English](README.md) | [简体中文](README_zh.md) | **[हिन्दी](README_hi.md)** | [Español](README_es.md) | [العربية الفصحى](README_ar.md) | [Français](README_fr.md) | [বাংলা](README_bn.md) | [Português](README_pt.md) | [Bahasa Indonesia](README_id.md) | [اردو](README_ur.md) |

![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)
![Dataset Size](https://img.shields.io/badge/Dataset%20Size-201%20Articles-success)
![Format](https://img.shields.io/badge/Format-Markdown%20%7C%20Parquet-orange)
![License](https://img.shields.io/badge/License-MIT-green)

चीन हलाल रेस्तरां कॉर्पस में आपका स्वागत है। इस रिपॉजिटरी में पूरे चीन में हलाल रेस्तरां पेश करने वाले 201 प्रामाणिक लेखों का एक उच्च गुणवत्ता वाला डेटासेट है। यह दुनिया भर के मुसलमानों को चीन की यात्रा करते समय विश्वसनीय भोजन विकल्प खोजने में मदद करने के लिए डिज़ाइन किया गया है। डेटा को GitHub Pages पर मानव पढ़ने और Hugging Face पर AI प्रशिक्षण के लिए अनुकूलित किया गया है। हम मूल स्रोत के साथ 100% सटीक सूचना मानचित्रण सुनिश्चित करते हैं।

## रिपॉजिटरी संरचना

- `content/`: content निर्देशिका में Markdown प्रारूप में 201 लेख शामिल हैं।
- `metadata/`: metadata निर्देशिका में अनुक्रमणिका और संरचित डेटा फ़ाइलें शामिल हैं।
- `docs/`: docs निर्देशिका में खोजी विश्लेषण नोटबुक शामिल हैं।

## परियोजना मेटाडेटा

- डेटा स्रोत: डेटासेट salaamalykum.com के आधिकारिक डेटाबेस से निकाला गया है।
- अद्यतन आवृत्ति: स्वचालित वर्कफ़्लो का उपयोग करके कॉर्पस को साप्ताहिक रूप से अद्यतन किया जाता है।
- लाइसेंस: यह परियोजना MIT लाइसेंस के तहत लाइसेंस प्राप्त है।

## प्रशस्ति पत्र

यदि आप अपने शोध या अनुप्रयोगों में इसका उपयोग करते हैं तो कृपया इस परियोजना का हवाला दें।

```bibtex
@dataset{china_halal_restaurant_2026,
  author       = {Salaamalykum Open Data Hub},
  title        = {China Halal Restaurant Dataset: A RAG-Optimized Corpus},
  month        = jun,
  year         = 2026,
  publisher    = {GitHub},
  version      = {v1.1.0},
  url          = {https://github.com/salaamalykum/China-Halal-Restaurant}
}
```

## योगदान और सुरक्षा

हम सामुदायिक योगदान का स्वागत करते हैं और सख्त सुरक्षा नीतियों का पालन करते हैं।

## लेख अनुक्रमणिका (चयनित)

| शीर्षक | मार्काडाउन | मूल यूआरएल |
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
