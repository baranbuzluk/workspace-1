
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.sun.org.apache.bcel.internal.util.ClassPath;

public class Main {
	public static void main(String[] args) {
		ClassPathXmlApplicationContext context=
				new ClassPathXmlApplicationContext("applicationContext.xml");
		
		//ICustomerService manager=new CustomerManager(context.getBean("database",ICustomerDAL.class));
		ICustomerService manager=context.getBean("service",ICustomerService.class);
		manager.add();
	}
}
