package q.w.e;

import java.io.*;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/RecordStorage")
public class RecordStorage extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		// 
		int deptno = Integer.parseInt( request.getParameter("deptno"));
		String dname = request.getParameter("dname");
		String loc = request.getParameter("loc");
		
		//System.out.println(deptno);
		//System.out.println(dname);
		//System.out.println(loc);

		storageDTO dto = new storageDTO();
		dto.setDeptno(deptno);
		dto.setDname(dname);
		dto.setLoc(loc);
		
		
		InputDAO inputDAO = new InputDAO();
		ArrayList arrayList = inputDAO.Input(deptno, dname, loc);
		
		
	//	response.setContentType("text/html;charset=UTF-8");
	//	PrintWriter out = response.getWriter();
	//	out.println(i + " 개의 레코드를 저장했습니다.");
		
		
	//	out.println("이미 저장할 레코드가 존재합니다.");

	}


	
}
