package q.w.e;

import java.io.*;
import java.sql.*;
import javax.naming.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import org.apache.commons.dbcp2.BasicDataSource;

@WebServlet("/DBpool")
public class DBpool extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	
		Connection connection = null;
		Boolean bool = true;
		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();
		try {
			Context context = new InitialContext();
			BasicDataSource basicDataSource = (BasicDataSource) context.lookup("java:comp/env/jdbc/oracledb");
			connection = basicDataSource.getConnection();
			if (bool == true) {
				out.println("연결되었습니다.");
			}
		} catch (Exception e) {
			out.println("연결에 실패했습니다.");
		} finally {
			try {
				connection.close( );
				} catch (SQLException e) {
				e.printStackTrace( );
			}
		}
	}
}