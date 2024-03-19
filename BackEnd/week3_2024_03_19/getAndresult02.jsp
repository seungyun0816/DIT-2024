<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>점수</h2>
	<%
		int korScore = Integer.parseInt(request.getParameter("kor")); //request.getParameter로 받은 문자열 자료형을 
																	  //Integer.parseInt로 숫자 자료형으로 변환 후 자바 변수 내 저장
		int engScore = Integer.parseInt(request.getParameter("eng"));
		
		int mathScore = Integer.parseInt(request.getParameter("math"));
		
		int average = (korScore + engScore + mathScore)/3;
		
		int total = korScore + engScore + mathScore;

		out.println("국어 점수:" + korScore);
		out.println("영어 점수:" + engScore);
		out.println("수학 점수:" + mathScore);
		out.println("평균:"+ average);
		out.println("총합:"+ total);
	%>
</body>
</html>