<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.time.*" %>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>2주차 2차시</title>
</head>
<body>
	<%@ include file="top.jsp" %><br>
	
	<h2>스크립트릿 부분</h2>
	<div id="mid">여긴 중앙.</div><br>
	<% out.println("Today : " + LocalDate.now() + "<br><br>"); %>
	
	<h2>표현식 부분</h2>
	<div id="tbox">Time:</div> <%= LocalTime.now() %>
	
<%@ include file="bot.jsp" %>
	
	<% /* JAVA주석 */ %>
	<!-- HTML주석 -->
	<%-- JSP주석 --%>
	
</body>
</html>