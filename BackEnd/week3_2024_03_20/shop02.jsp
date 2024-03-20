<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
	
		String[] lang = request.getParameterValues("lang");
		String[] hobby = request.getParameterValues("hobby");
		
		//1.배열의 index번호를 통해 출력
		//여러 값이 담긴 배열의 index번호로 출력
		for(String s : hobby){
			out.println(s);
		}
		
		//2.배열에 담긴 객체를 각각 순서대로 출력
		//for(a:b) a에 b를 담는다. b에서 더 이상 꺼낼 객체가 없을 떄 까지.
		//out.println에서 바로 담긴 값을 출력하고, 다음 값으로 덮어씌운다음 출력된다.
		
		
		/* for(String s : hobby){
			out.println(s);
		} */
		
		for(String s : lang){
			out.println(s);
		}
	%>
</body>
</html>