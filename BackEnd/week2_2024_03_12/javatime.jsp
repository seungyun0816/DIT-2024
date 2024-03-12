<%@ page language="java" contentType="text/html; charset=EUC-KR"	//페이지의 설정을 정의하기
    pageEncoding="UTF-8"%>		
<%@ page import="java.time.*" %> 					//java.time 패키지 불러오기
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
		out.println("Today : " + LocalDate.now() + "<br>");
		out.println("Time : " + LocalTime.now());
	%>
</body>
</html>
