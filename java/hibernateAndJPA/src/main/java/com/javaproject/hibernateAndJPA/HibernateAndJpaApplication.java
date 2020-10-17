package com.javaproject.hibernateAndJPA;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan({ "com.javaproject.hibernateAndJPA.business", "com.javaproject.hibernateAndJPA.DataAcces" ,"com.javaproject.hibernateAndJPA.restApi"}) 
public class HibernateAndJpaApplication {

	public static void main(String[] args) {
		SpringApplication.run(HibernateAndJpaApplication.class, args);
	}

}
