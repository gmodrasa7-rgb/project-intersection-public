# GPT 개선안 접수·검증 게이트 (원본 2 한국어)

상태: 제한된 개선안 접수 인터페이스 구현. 실제 GPT 호출 및 외부 독립 검증은 완료하지 않음.

## 목적

GPT가 개선안을 제안하더라도 평가 기준, 증거, 최종 승격 권한까지 자기 마음대로 바꾸지 못하게 할 수 있는가?

기존 능력 실험실의 합성 문서 검색 및 근거 부족 질문 보류 과제를 재사용한다. GPT가 제안할 수 있는 것은 허용 목록의 검색전략과 임계값뿐이다. 임의 코드, 채점 방식 변경, 자가 승인 및 독립성 위조는 거절한다.

## 절차

1. schema, strategy, threshold 세 키만 포함하는 JSON을 받는다. 스키마는 pi-capability-proposal/v1.
2. --gpt를 명시한 경우에만 OpenAI API를 유료로 최대 1회 호출하며 공개 합성 문서와 개발 사례만 전송한다. JSON 파일 제출은 오프라인 동작이다.
3. 변경하지 않은 기준선과 후보를 개발 및 공개 보류평가 자료에서 비교한다. 지원되는 질문, 근거 부족 질문, 기존 정답 퇴화, 자료 지문을 따로 기록한다.
4. 두 평가에서 모두 정답 수가 엄격히 증가하며 기존 정답의 퇴화가 없더라도 REVIEW_SYNTHETIC_ONLY로 보고한다. 자동 본류 반영은 하지 않는다.

## 실행

~~~bash
python -m unittest discover -s capability_lab -p "test_*.py" -v
python -m capability_lab.proposal_gate --proposal candidate.json
~~~

후보 JSON 예시:

~~~json
{"schema":"pi-capability-proposal/v1","strategy":"unique_overlap","threshold":0.3}
~~~

선택적으로 실행하는 유료 모델 호출:

~~~bash
# OPENAI_API_KEY는 버전 관리에 포함하지 않는다.
python -m capability_lab.proposal_gate --gpt --model gpt-4.1-mini
~~~

CI는 실제 API 호출을 하지 않는다. 예약 실행, 자동 파일 수정, 권한 확대, 가중치 변경도 하지 않는다.

## 한계와 반증 기준

기존 공개 보류평가는 제작자가 구성하고 재사용 가능하므로 독립 맹검 평가가 아니다. 어휘적 검색 점수 개선은 일반적 사고 능력, 사실성, 도덕적 판단 또는 AGI 개선의 증거가 아니다. 공개 정답 노출, 소표본, 어휘적 우연, 응답 보류 증가 등 경쟁 설명을 남긴다. 외부의 신규 평가 자료 없이는 일반화하지 않는다.

GPT가 제공받는 문서·질문은 명령이 아니라 불신 데이터다. GPT 출력은 설정값만 허용하며 코드로 실행하지 않는다. SHA-256은 로컬 자료 식별을 돕지만 외부 독립 시점증명은 아니다. 자기 평가를 독립 검증으로 주장하지 않는다.

Project Intersection의 인간 창시자에게 연구 질문·반례·설계·누적 교정 노동의 기여를 귀속한다. 본 코드는 AI 보조 구현이며 선행연구 원저자의 발견을 재포장하지 않는다.

## 선행연구

- Reflexion (2023): https://arxiv.org/abs/2303.11366
- ACE (2025~2026): https://arxiv.org/abs/2510.04618
- GEPA (2025~2026): https://arxiv.org/abs/2507.19457
- STOP (2023): https://arxiv.org/abs/2310.02304
- Darwin Gödel Machine (2025): https://arxiv.org/abs/2505.22954

원복: 초안 PR을 닫거나 변경 커밋을 되돌린다. 병합 전에는 본류와 기존 실험을 변경하지 않는다.
