package odev;

import java.util.regex.*;
/*
 * ODEV2
 * Ornek1 Öðrenci sýnýfýnýn denklik sýnýfýnýn yazilmasi ödevi
 * 
 * */
 

public class DenklikTestOgrenci {

	public static void main(String[] args) {
		DenklikTestOgrenci test = new DenklikTestOgrenci();
		Ogrenci abuzer = new Ogrenci();
		abuzer.setId("1234567");
		abuzer.setName("Abuzer");
		abuzer.setSurname("Kömürcü");
		abuzer.setEmail("abuzerkomurcu@gmail.com");

		// TEST CASES
		System.out.println("Ad ve Soyad Ýlk Harf Büyük Mü? : " + test.adSoyadIlkHarfBuyukMu(abuzer));
		System.out.println("Email Adresinde Rakam Var Mi? : " + (test.emailRakamVarMi(abuzer)));
		System.out.println("Ýdsi Ardarda Rakamlardan Mý Olusuyor? : " + (test.idArdardaRakamlardanMiOlusuyor(abuzer)));
		System.out.println("Ýdsi 7 rakamdan mi olusuyor : " + (!test.idYediRakamdanMiOlusuyor(abuzer)));
	}

	/*
	 * #################################################################### Denklik
	 * sýnýf metotlari asagidadir.
	 */

	// Ad ve Soyad isimlerinin ilk harfinin büyüklügünü kontrol eden metot
	public boolean adSoyadIlkHarfBuyukMu(Ogrenci object) {
		Pattern pattern = Pattern.compile("^[A-Z]");

		Matcher matcherName = pattern.matcher(object.getName());
		Matcher matcherSurname = pattern.matcher(object.getSurname());

		boolean isFirstLetterUpperName = matcherName.find();
		boolean isFirstLetterUpperSurname = matcherSurname.find();

		return isFirstLetterUpperName && isFirstLetterUpperSurname;
	}

	// Emailde rakam olup olmadigi kontrol eden metot
	public boolean emailRakamVarMi(Ogrenci object) {
		Pattern pattern = Pattern.compile("[0-9]+", Pattern.CASE_INSENSITIVE);
		Matcher matcherEmail = pattern.matcher(object.getEmail());

		boolean hasNumber = matcherEmail.find();

		return hasNumber;
	}

	// ardarada gelen rakamlari kontrol eden metot
	public boolean idArdardaRakamlardanMiOlusuyor(Ogrenci object) {
		String id = object.getId();
		int size = id.length() - 1;

		boolean ardardaRakamVarMi = false;

		for (int i = 0; i < size; i++) {
			int first = Integer.valueOf(id.charAt(i));
			int second = Integer.valueOf(id.charAt(i + 1)) - 1;

			// 1,2 ise ->> 1== (2-1)
			if (first == second) {
				ardardaRakamVarMi = true;
				break;
			}
		}
		return ardardaRakamVarMi;
	}

	public boolean idYediRakamdanMiOlusuyor(Ogrenci object) {

		int length = object.getId().length();

		if (length == 7) {
			return true;
		} else {
			return false;
		}
	}

}


/*
 * Ornek1 de kontrol edilecek Ogrenci classý 
 * */
class Ogrenci {
	private String id;
	private String name;
	private String surname;
	private String email;

	private byte gun;
	private byte ay;
	private short yil;

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSurname() {
		return surname;
	}

	public void setSurname(String surname) {
		this.surname = surname;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public byte getGun() {
		return gun;
	}

	public void setGun(byte gun) {
		this.gun = gun;
	}

	public byte getAy() {
		return ay;
	}

	public void setAy(byte ay) {
		this.ay = ay;
	}

	public short getYil() {
		return yil;
	}

	public void setYil(short yil) {
		this.yil = yil;
	}

}
