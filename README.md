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
    <a href="https://doi.org/10.5281/zenodo.10158254"><img alt="DOI" src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.10158254-blue"></a>
</p>

## How to use

🤗 [Huggingface Hub](https://huggingface.co/oneonlee/KoAirBERT/tree/main)에 업로드 된 모델을 바로 사용할 수 있습니다 :)

```python
# Load model directly
from transformers import AutoTokenizer, AutoModelForPreTraining

tokenizer = AutoTokenizer.from_pretrained("oneonlee/KoAirBERT")
model = AutoModelForPreTraining.from_pretrained("oneonlee/KoAirBERT")
```

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
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.10158254},
  url          = {https://doi.org/10.5281/zenodo.10158254}
}
```

## License

`KoAirBERT`는 `AGPL-3.0` 라이선스 하에 공개되어 있습니다. 모델 및 코드를 사용할 경우 라이선스 내용을 준수해주세요. 라이선스 전문은 [LICENSE 파일](LICENSE)에서 확인하실 수 있습니다.
