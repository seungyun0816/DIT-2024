<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<form action="shop02.jsp" method="get">
		관심언어
		<input type="checkbox" name="lang" value="RUST">RUST	<!-- 한 가지 name(lang)으로 묶인 데이터 배열 전송 -->
		<input type="checkbox" name="lang" value="JAVA">JAVA
		<input type="checkbox" name="lang" value="C#">C#
		<br>
		취미
		<select name="hobby" size="4" multiple>
			<option value="movie">영화</option>
			<option value="game">게임</option>
			<option value="music">음악</option>
			<option value="book">독서</option>
		</select>
		<input type="submit" value="전송">
	</form>
</body>
</html>