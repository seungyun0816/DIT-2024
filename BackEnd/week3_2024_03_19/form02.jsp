<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>Welcome!!!</h2>
	<% request.setCharacterEncoding("UTF-8"); //method속성의 POST형식 데이터 response의 경우 한글이 깨지기 때문에 Encoding형식을 지정해야함
	
		String id =request.getParameter("id");		//form01에서 가져온 데이터를 문자열 변수에 저장
		String name = request.getParameter("name");
		String pwd = request.getParameter("pwd");
		
		out.println(id);	//문자열 변수에 저장 된 값 출력
		out.println(name);
		out.println(pwd);
	%>
	<form action="form01.jsp" method="get">
		<input type="submit" value="돌아가기">
	</form>
</body>
</html>