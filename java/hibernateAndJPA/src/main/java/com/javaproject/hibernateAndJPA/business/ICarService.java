package com.javaproject.hibernateAndJPA.business;

import java.util.List;

import com.javaproject.hibernateAndJPA.Entities.Car;

public interface ICarService {
	List<Car> getAll();
	void add(Car item);
	void update (Car item);
	void delete(Car item);
}
