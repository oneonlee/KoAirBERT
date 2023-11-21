<!---
Copyright (C) 2023 Donggeon Lee
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.
 
You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
-->

<div align="center">
    <h1>🤗 KoAirBERT  ✈️</h1>
    <p>항공 안전 도메인에 특화된 한국어 BERT 모델</p>
</div>
    
<p align="center">
    <img alt="Python" src="https://img.shields.io/badge/python-3.8-blue.svg">
    <a href="https://huggingface.co/oneonlee/KoAirBERT"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97-Models%20on%20Hub-yellow"></a>
    <a href="https://github.com/oneonlee/KoAirBERT/blob/master/LICENSE"><img alt="License: AGPL-v3" src="https://img.shields.io/badge/License-AGPL--v3-blue.svg"></a>
    <a href="https://doi.org/10.5281/zenodo.10171038"><img alt="DOI" src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.10171038-blue"></a>
</p>

## How to use

🤗 [Huggingface Hub](https://huggingface.co/oneonlee/KoAirBERT/tree/main)에 업로드 된 모델을 바로 사용할 수 있습니다 :)

```python
# Load model directly
from transformers import AutoTokenizer, AutoModelForPreTraining

tokenizer = AutoTokenizer.from_pretrained("oneonlee/KoAirBERT")
model = AutoModelForPreTraining.from_pretrained("oneonlee/KoAirBERT")
```

## Post-training

KoAirBERT는 [klue/bert-base](https://huggingface.co/klue/bert-base) 모델에 MLM 및 NSP 방식의 Post-training을 추가로 수행한 모델입니다.<br>
학습에는 직접 구축한 [한국어 항공안전 도메인 데이터셋](#dataset-info)을 사용했고, NVIDIA RTX A6000 48GB 1장을 사용하여 약 40분 소요되었습니다.<br>
학습 세팅은 아래와 같습니다.

| Params | Initial learning rate | Batch Size | Epochs | Max length\* | Weight decay |
| :-- | :--: |  :--: | :--: | :--: | :--: |
| 111M | 5e-5 | 8 | 3 | 512 | 0.01 |

## Dataset Info.

|     데이터 명                                   |     데이터 건 수    |     문장 수    |       단어 수    |
|:-------------------------------------------------|--------------------:|---------------:|-----------------:|
|     사고·준사고보고서                           |               54    |       1,850    |        33,935    |
|     안전장애 보고 데이터                        |              684    |      10,018    |        69,472    |
|     고장 보고 데이터                            |            1,771    |      10,480    |        85,165    |
|     국토교통부 항공용어사전                     |            4,961    |      15,312    |       167,295    |
|     항공안전문화지표 분석 데이터                |            1,055    |       3,652    |       244,032    |
|     항공안전문화지표 분석 데이터 – 본문 증강    |            5,902    |      56,193    |     1,055,875    |
|     GYRO 항공 안전 자율 보고서                  |              874    |      10,655    |       158,186    |
|     항공위키                                   |               4,314 |         38,927 |          766,214 |
|-----------------------------------------------|--------------|--------|----------|
|     **누적**                                        |           **19,615**    |     **147,087**    |     **2,580,174**    |

## Reference

- [BERT](https://arxiv.org/abs/1810.04805)
- [klue/bert-base](https://huggingface.co/klue/bert-base)
- [huggingface/transformers](https://github.com/huggingface/transformers/) - pytorch [language-modeling](https://github.com/huggingface/transformers/tree/main/examples/pytorch/language-modeling) examples
- [항공 안전 정보지 (GYRO)](https://www.airsafety.or.kr/airsafety/board/gyro/list.do)
- [항공위키](https://airtravelinfo.kr/wiki/)
- [국토교통부 항공용어사전](https://www.airportal.go.kr/knowledge/library/KdMain01.jsp)
- [항공안전 자율보고 백서(2021)](https://www.airsafety.or.kr/airsafety/board/aspds/view.do?bbsNo=4431)

## Citation

이 코드를 연구용으로 사용하는 경우 아래와 같이 인용해주세요.

```bibtex
@software{lee_2023_10158254,
  author       = {Lee, DongGeon},
  title        = {KoAirBERT: Korean BERT Model Specialized for Aviation Safety Domain},
  month        = nov,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v1.0.1},
  doi          = {10.5281/zenodo.10171038},
  url          = {https://doi.org/10.5281/zenodo.10171038}
}
```

## License

`KoAirBERT`는 `AGPL-3.0` 라이선스 하에 공개되어 있습니다. 모델 및 코드를 사용할 경우 라이선스 내용을 준수해주세요. 라이선스 전문은 [LICENSE 파일](LICENSE)에서 확인하실 수 있습니다.
