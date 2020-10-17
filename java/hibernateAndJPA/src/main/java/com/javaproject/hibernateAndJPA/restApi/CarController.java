package com.javaproject.hibernateAndJPA.restApi;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.javaproject.hibernateAndJPA.Entities.Car;
import com.javaproject.hibernateAndJPA.business.ICarService;

@RestController
@RequestMapping("/api")
public class CarController {
	
	private ICarService service;

	@Autowired
	public CarController(ICarService service) {
		super();
		this.service = service;
	}
	
	@GetMapping("/cars")
	public List<Car> get(){
		return service.getAll();
	}

}
