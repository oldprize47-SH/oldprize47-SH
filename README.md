# 박상헌

[한국어](#korean) · [English](#english)

<a id="korean"></a>
## 한국어

전자제어공학과 컴퓨터공학을 공부했습니다. 임베디드 소프트웨어, 제어, 로보틱스 분야의 인턴·신입 직무를 준비하고 있습니다.

처음 방문하셨다면 자율비행 드론, 임베디드 제어, 모터 시스템 식별 프로젝트부터 보시면 됩니다. 각 README에는 프로젝트 목표와 구성, 팀원별 작업, 실행 방법, 확인한 결과와 한계를 정리했습니다. 같은 과목에서 진행한 구성요소는 하나의 대표 프로젝트로 묶었습니다.

### 주요 프로젝트

- [자율비행 드론 프로젝트](https://github.com/oldprize47-SH/Autonomous_Drone_Development): 기체, 제어기, 비행 소프트웨어, 지상국과 RealSense 착륙 표식 인식을 통합한 팀 프로젝트입니다. 저는 비전 데이터 수집·라벨링, 모델 비교, 임베디드 추론, 추적과 비행제어부에 전달할 관측 정보를 담당했습니다. 반복 가능한 정밀 착륙은 입증하지 못했습니다. 표식 인식은 별도 프로젝트가 아니라 이 프로젝트의 비전 구성요소입니다.
- [임베디드 제어 프로젝트](https://github.com/oldprize47-SH/stm32-embedded-controller): STM32 주변장치 실습과 RC카·자동 분리수거함을 함께 정리했습니다. C, 타이머, PWM, 센서 입력과 직렬 통신을 실제 장치 동작에 연결합니다. [분리수거함 팀 시연](https://www.youtube.com/watch?v=dkphMHEKzxE)도 확인할 수 있습니다.
- [모터 시스템 식별](https://github.com/oldprize47-SH/motor-system-identification): 김찬중과 측정·모델 식별·제어기 설계 과정을 함께 수행한 프로젝트입니다. 저는 측정 환경과 보정, 응답 데이터 수집에서 먼저 동작하는 결과를 얻었습니다. MATLAB/Simulink 분석, 기록된 데이터와 응답 플롯 재현 스크립트가 포함돼 있습니다.
- [시선 추적 마우스](https://github.com/oldprize47-SH/gaze-mouse-course-project): 웹캠 영상으로 마우스 포인터를 움직이고 시선 유지·눈 깜빡임으로 클릭하는 프로젝트입니다. 저는 데이터와 모델, 보정, 포인터·클릭 동작과 평가를 담당했고 김선우는 키보드 구성요소와 발표자료를 맡았습니다.
- [졸업연구 · 모델링과 실험 검증](https://github.com/oldprize47-SH/Capstone-Research-Portfolio): 연구 역할, 시험 프레임에서의 시연과 학술 기록을 정리했습니다. 프레임 시험과 실제 비행의 검증 범위를 구분합니다.

### 다른 수업 프로젝트

- [알고리즘 분석](https://github.com/oldprize47-SH/algorithm-analysis): C++ 과제 다섯 개와 일부 경계 조건의 회귀 테스트.
- [운영체제 실습](https://github.com/oldprize47-SH/operating-systems-labs): C로 작성한 프로세스, 파이프, 읽기·쓰기 동기화와 스레드 파일 검색 실습.
- [영상처리 실습](https://github.com/oldprize47-SH/image-processing-labs): 기어·색상·띠 형상·차선의 영상 특징을 다루는 OpenCV 실습.
- [AI·데이터 분석 실습](https://github.com/oldprize47-SH/ai-coursework): 주차별 노트북과 저장된 출력.
- [상품 리뷰 웹 애플리케이션](https://github.com/oldprize47-SH/ceneo-review-webapp)과 [데이터 분석](https://github.com/oldprize47-SH/ceneo-review-analysis): Flask 웹 화면과 Python 분석 노트북.
- [축구 라인업 웹사이트](https://github.com/oldprize47-SH/football-lineup-web): HTML 페이지와 이미지 연결을 연습한 초기 웹 프로젝트.

이전 저장소 이력에는 `oldprize47` 또는 `sangheon47` 계정이 사용됐습니다. 이 계정은 포트폴리오 열람을 위해 프로젝트를 모은 곳입니다. 팀 기여와 수업 제공 자료의 출처는 각 저장소에 구분했으며, 일부 구현과 실험에는 AI 코딩 도구를 활용했습니다.

---

<a id="english"></a>
## English

**Sangheon Park**

I studied electronic control engineering and computer science. I am interested in embedded software, control and robotics, and am looking for internship and graduate engineering roles.

If you are visiting for the first time, start with the autonomous drone, embedded control and motor-identification projects. Each README explains the goal, system configuration, team responsibilities, how to run the work, and its results and limits. Components from the same course project are grouped under one main project.

### Selected projects

- [Autonomous Drone Project](https://github.com/oldprize47-SH/Autonomous_Drone_Development): a team platform combining the aircraft, control, flight software, ground station and RealSense landing-marker vision. I handled vision data collection and labelling, model comparisons, embedded inference, tracking and target observations for the flight controller. Repeatable precision landing was not demonstrated. Marker vision is a component of this project, not a separate project.
- [Embedded Control Projects](https://github.com/oldprize47-SH/stm32-embedded-controller): STM32 peripheral exercises, an RC car and an automatic recycling system. The work connects C, timers, PWM, sensor inputs and serial communication to physical mechanisms. A [team demonstration](https://www.youtube.com/watch?v=dkphMHEKzxE) shows the recycling prototype.
- [Motor System Identification](https://github.com/oldprize47-SH/motor-system-identification): 김찬중 and I both worked through measurement, identification and controller design. I first obtained working results for measurement setup, calibration and response-data collection. The repository includes MATLAB/Simulink analysis, recorded data and a script to reproduce the response plot.
- [Gaze-Controlled Mouse](https://github.com/oldprize47-SH/gaze-mouse-course-project): a webcam-based pointer interface with calibration, gaze-hold and blink interaction. I handled the data, model, calibration, pointer and click behaviour, and evaluation. 김선우 developed the keyboard component and prepared the presentation materials.
- [Capstone Research: Modelling and Experimental Validation](https://github.com/oldprize47-SH/Capstone-Research-Portfolio): research responsibilities, test-frame demonstrations and academic records. The documentation distinguishes constrained-frame tests from flight validation.

### Other coursework

- [Algorithm Analysis](https://github.com/oldprize47-SH/algorithm-analysis): five C++ coursework programs and regression tests for selected boundary cases.
- [Operating Systems Labs](https://github.com/oldprize47-SH/operating-systems-labs): process, pipe, reader/writer and threaded file-search exercises in C.
- [Image Processing Labs](https://github.com/oldprize47-SH/image-processing-labs): OpenCV exercises involving gear geometry, colour regions, strip shape and lane features.
- [AI and Data Analysis Labs](https://github.com/oldprize47-SH/ai-coursework): weekly notebooks and saved outputs.
- [Product Review Web App](https://github.com/oldprize47-SH/ceneo-review-webapp) and [Product Review Analysis](https://github.com/oldprize47-SH/ceneo-review-analysis): Flask and Python coursework.
- [Football Lineup Website](https://github.com/oldprize47-SH/football-lineup-web): an early HTML project connecting pages and images.

Earlier repository history uses `oldprize47` or `sangheon47`. This account brings the projects together for portfolio review. Team contributions and course material are identified in each repository. AI coding tools supported parts of my implementation and experiments.
