function doSumething() {
    // 잘 호출되는지 확인
    // 팝업 안내창 띄우기
    // alert("잘 호출쓰~");
    // input 텍스트 박스의 값 조회하기
    // document : html 문서 전체를 document라고 칭한다
    // getElementById : 태그 id 속정이 값이 괄호()안에 있는 값인 찾기
    // value : 텍스트박스에 입력되어 있는 값 - 문자열값
    a = document.getElementById("inputA").value;
    b = document.getElementById("inputB").value;
    // 조회 확인
    // alert(a)
    // alert(b)
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueB").innerHTML = b;
    document.getElementById("valueC").innerHTML = Number(a)+Number(b);
}
// 시간 안내 띄우기
function viewTime(){
    // 호출확인
    alert(new Date());
}