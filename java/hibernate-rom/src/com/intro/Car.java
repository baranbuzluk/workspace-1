package com.intro;

import javax.persistence.*;

@Entity
@Table(name="cars")
public class Car {
	@Id
	private Integer carId;
	
	
	private String carCompanyName;
	private String carLicense;
	public Integer getCarId() {
		return carId;
	}
	public void setCarId(Integer carId) {
		this.carId = carId;
	}
	public String getCarCompanyName() {
		return carCompanyName;
	}
	public void setCarCompanyName(String carCompanyName) {
		this.carCompanyName = carCompanyName;
	}
	public String getCarLicense() {
		return carLicense;
	}
	public void setCarLicense(String carLicense) {
		this.carLicense = carLicense;
	}
	
}
