## SaaS, PaaS, IaaS

- SaaS

  - Software as a Service
  - 필요한 SW를 비용을 지불하고 어디서든 곧바로 쓸 수 있다는 장점
  - 클라우드 환경에서 운영되기에, SW를 설치할 필요 없이 구입하는 즉시 웹에서 사용 가능
  - 보통 흔히들 알고있는 클라우드 서비스
  - 레고모형

- IaaS

  - Infrastructure as a Service
  - 개발자는 데이터를 인터넷 서버와 스토리지에 저장해두고 사용자는 클라우드 환경에서 필요한 인프라를 꺼내서 설치하고 사용할 수 있음
  - 레고공장

- PaaS

  - Platform as a Service
  - 필요한 서비스를 선택해서 어플리케이션을 개발 가능
  - 레고 블록

  

## 클라이언트사이드

- 모든 렌더링이 끝난 후 데이터 변화가 발생하면 이를 처리하기 위해서 클라이언트 사이드 작업이 필요하다
- 장점
  - 많은 연산이 필요한 서비스의 경우 모든 연산은 back에서 하게 된다면, 서버처리의 부담이 증가하고 서버 비용증가가 발생, 이를 해결하기 위해 클라이언트 사이드 연산이 필요
  - 보안에 민감한 데이터의 경우 클라이언트 사이드 내에서 처리한다면, 통신 중에 발생하는 해킹에 대비할 수 있음
- 단점
  - 사용자 컴퓨터의 처리 부담이 증가
  - 서버 측에서 클라이언트 사이드 연산 결과의 진위를 파악하기 힘듬

## HTTP Protocol

- 정의
  - 프로토콜이란 상호간에 정의한 규칙을 의미하며, 특정 기기간에 데이터를 주고 받기 위해 정의 된것

- 특징
  - 모든 데이터 통신이 서로 독립적임
  - 다수의 요청 처리 및 서버의 부하를 줄일 수 있는 성능상의 이점이 생김
  - 일반적으로 TCP/IP 통신 위에서 동작하며 기본 포트는 80
- Methods
  - GET : 존재하는 자원에 대한 요청
  - POST : 새로운 자원 생성
  - PUT : 존재하는 자원에 대한 변경
  - DELETE : 존재하는 자원에 대한 삭제
  - HEAD : 서버 헤더 정보를 획득. GET과 비슷하나 Response Body를 반환하지 않음
  - OPTION : 서버 옵션을 확인하기 위한 요청. CORS에서 사용
- 상태코드
  - 2xx : 성공
  - 3xx : 리다이렉트 유도
  - 4xx : 클라이언트 에러
  - 5xx : 서버에러
- 요약
  - 브라우저에서 URL + 요청 Methods로 HTTP Request를 보내면
  - 서버에서 상태코드 + Response Body로 HTTP Response를 보내줌



## JAVASCRIPT

- ### 이벤트 위임

  - 이벤트 리스너를 각각의 클래스에 모두 생성하는게 아니라
  - 한개의 이벤트 리스너를 전체 영역에 대해 등록하는것이 효율적

  

- ### 클로져

  - 독립적인 변수를 가리키는 함수, 클로저 안에 정의된 함수는 만들어진 환경을 기억한다.

  - 흔히들 함수내의 함수를 의미함

    - 비공개 변수를 가질 수 있는 환경에 있는 함수

  - 변수 은닉화에 사용됨
    
    - 함수에 직접 접근하여 변수를 변조할 가능성이 있기에 이를 방지하기 위해서 클로져를 통한 은닉화 적용
    
  - 잘못된 사용으로 인해 성능, 메모리 문제를 야기시킬 수 있음

  - ```javascript
    var lst = [1, 2, 3, 4]
    for (var i = 0; i < lst.length; i++) {
      console.log("aaaaaaa", i)
    
      // setTimeout(function() {
      //   console.log(i)
      // }, 2000)
    
      setTimeout(function(a) {
        console.log("bbbbbb", a)
        // 아래 함수가 클로져
        return function() {
          console.log(a)
        }
      }(i), 2000)
      // IIFF(즉시 함수 호출 표현식)
      // 라이브러리를 만들때 사용함
      
      // setTimeout(function(i) {
      //   return function() {
      //     console.log(i)
      //   }
    // }(i), 2000)
    }
    ```
    
    

  

- ### 디바운싱

  - 연이어 호출되는 함수들 중 마지막 or 처음만 호출하도록 하는 것

    - 순차적 호출을 그룹화하여 특정시간이 지난 후 하나의 이벤트만 발생

  - 주로 ajax에 활용(?)
  
    - 비용문제와 연결됨
  
  - ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <input type="text" id="input">
        <script>
            var timer
            const input = document.querySelector("#input")
            input.addEventListener("input", function(e) {
                if (timer) {
                    console.log("ccccccccccc")
                    clearTimeout(timer)
                };
            // 클로저를 활용함
                timer = setTimeout(function() {
                    console.log(e.target.value)
                }, 200)
            })
      </script>
    </body>
  </html>
    ```



- ### 쓰로틀링

  - 마지막 함수가 호출 된 후 일정 시간이 지나기 전에 다시 호출되지 않도록 하는 것

    - 이벤트를 일정 주기마다 발생하도록 하는것

  - 주로 스크롤이벤트에 사용(?)

    - 성능 문제와 연결됨

  - ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <input type="text" id="input">
        <script>
            // 쓰로틀링
            var timer;
            const input = document.querySelector("#input")
            input.addEventListener("input", function(e) {
                console.log(timer)
                if (!timer) {
                    // 클로저 활용
                    timer = setTimeout(function() {
                        timer = null;
                        console.log(e.target.value)
                    }, 2000)
                }
            });
        </script>
    </body>
    </html>
    ```

  - 



- ### 호이스팅

  - 함수안에 있는 선언들을 모두 끌어올려 해당 함수 유효범위의 최상단에 선언하는것
  - 나중에 선언된 변수를 참조할 수 있음
  - 변수와 함수를 위한 메모리를 확보하는 과정에서 발생
  - var 변수, 함수의 선언에서 호이스팅이 발생



- ### 네임스페이스

  - 변수명 겹침 현상을 방지하기 위해서 사용
  - 사용할 변수를 전역 변수가 아닌 함수안의 지역변수로 만듬
  - 누군가 고의적으로 접근하여 변수명을 바꿀 수 있으므로, 클로저를 활용하여 은닉화
