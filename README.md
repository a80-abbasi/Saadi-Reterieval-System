# Saadi1401-5_23
1401/Spring/InformationRetrieval/g5+23

## Elastic Search
To use this service first you need to download and run elastic search engine from [here](https://www.elastic.co/downloads/elasticsearch) (version `7.8.1` is recommended).

For this project we use `parsi` analyzer (thanks to [NarimanN2](https://github.com/NarimanN2/ParsiAnalyzer#build)) for our index so you need to download and add this plugin to your elastic engine. If you have elastic version `7.8.1` you can download it from [here](https://drive.google.com/file/d/1yqCDjcydati3s4BRda4c3kiGXoNGshGU/view?usp=sharing) and follow step 8 of [this](https://github.com/NarimanN2/ParsiAnalyzer#build) link. If you have version `7.13.1` you can use [this](https://github.com/NarimanN2/ParsiAnalyzer#installation) link. If you have another version of elastic engine you need to download and complie the code of this plugin from [here](https://github.com/NarimanN2/ParsiAnalyzer#build) for your own elastic version (note: if you have problem with step 8 in the previous link, just unzip file and copy its content to `{your-elastic-path}/plugins/farsi/`).
