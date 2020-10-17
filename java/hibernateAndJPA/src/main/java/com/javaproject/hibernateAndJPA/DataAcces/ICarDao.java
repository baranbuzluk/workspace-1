package com.javaproject.hibernateAndJPA.DataAcces;

import java.util.List;

import com.javaproject.hibernateAndJPA.Entities.Car;

public interface ICarDao {
List<Car> getAll();
void add(Car item);
void update (Car item);
void delete(Car item);

}
