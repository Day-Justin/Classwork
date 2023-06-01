import java.math.BigInteger;
import java.util.*;
import java.io.*;

public class quadratic_sieve {
	
	public static BigInteger zero = new BigInteger("0");
	public static BigInteger one = new BigInteger("1");
	public static BigInteger two = new BigInteger("2");
	
	public static BigInteger powersOfTwo(BigInteger n) {
		
		BigInteger x = new BigInteger("0");
		
		// while even
		while(n.mod(two).equals(zero)) {
			
			n = n.divide(two);
			x = x.add(one);
			
		}
		
		return x;
		
	}
	
	public static BigInteger shanksTonelli(BigInteger n, BigInteger p, long start) {
		
		// p - 1 = Q * 2^S
		BigInteger S = powersOfTwo(p.subtract(one));
		
		// Q = (p - 1) / 2^S
		BigInteger Q = (p.subtract(one)).divide(two.pow(S.intValue()));
		
		// now we need to find a quadratic non-residue
		// we will use euler's criterion
		BigInteger z = zero;
		
		BigInteger loop = one;
		
		for(loop = one; loop.compareTo(p) == -1 ; loop = loop.add(one)) {
			
			// if (i ^ ( p-1 / 2 ) ) mod p == p - 1
			// that means it equals -1 mod p
			// which makes i an quadratic non-residue
			if(loop.modPow((p.subtract(one)).divide(two), p).equals(p.subtract(one))) {
				z = loop;
				break;
			}
			
		}
		
		// let M = S, c = z^Q, t = n^Q, R = n ^ ( Q+1 / 2) all mod p
		BigInteger M = S.mod(p);
		BigInteger c = z.modPow(Q, p);
		BigInteger t = n.modPow(Q, p);
		BigInteger R = n.modPow((Q.add(one)).divide(two), p);
		
		// if t = 0, return r = 0
		// if t = 1, return r = R
		// give while loop 100ms and if it doesn't compute, return 0
		while( ( (System.nanoTime() - start) / 100 ) < 1000) {
			
			if(t.equals(zero))
				return zero;
			
			if(t.equals(one))
				return R;
			
			int i = 1;
			
			// while t^2^i != 1, increment i
			while(!(t.pow(2).pow(i).mod(p).equals(one))) {
			// repeated squaring to find the least i , 0 < i < M, such that t ^ 2 ^i = 1 mod p
				i++;
			}
			
			BigInteger newI = new BigInteger(Integer.toString(i));
			
			// b = c ^ 2 ^ M-i-1 mod p
			// same as c*c ^ M-i-1 mod p
			// this line gave me problems when i was 
			BigInteger b = c.pow((int) Math.pow(2, M.intValue() - i - 1)).mod(p);
			
			M = newI.mod(p);
			c = (b.multiply(b)).mod(p);
			t = (t.multiply(b).multiply(b)).mod(p);
			R = (R.multiply(b)).mod(p);
			
		}
		
		return zero;
		
	}
	
	
	static BigInteger GCD(BigInteger m, BigInteger n) {
		
		BigInteger zero = new BigInteger("0");
		BigInteger r;
		
		// if (m < n), swap m and n
		if(m.compareTo(n) == -1) {
			BigInteger temp = m;
			m = n;
			n = temp;
		}
		
		// while n != 0
		while(!n.equals(zero)) {
			
			r = m.mod(n);
			m = n;
			n = r;
			
		}
		
		return m;
		
	}
	
	static BigInteger pollardRho(BigInteger n) {
	
		if(n.mod(two).equals(zero))
			return two;
		
		BigInteger five = new BigInteger("5");
		
		if(n.mod(five).equals(zero))
			return five;
		
		BigInteger one = new BigInteger("1");
		
		BigInteger base = two;
		BigInteger constant = one;
		BigInteger t = base;
		BigInteger h = base;
		
		// while d doesn't change, do steps
		while(true) {
			
			// g(x) = (x^2 + 1) mod n
			
			// x = g(x)
			t = ((t.pow(2)).add(constant)).mod(n);
			
			// y = g(g(y))
			h = ((h.pow(2)).add(constant)).mod(n);
			h = ((h.pow(2)).add(constant)).mod(n);
			
			// compute |x-y|
			BigInteger abs = ((t.subtract(h)).abs());
			
			BigInteger d = GCD(abs, n);
			
			if(d.compareTo(one) == 1)
				return d;
			else if(d.equals(n)) {
				
				base = base.multiply(two);
				constant = constant.multiply(two);
				t = base;
				h = base;
				
			}
			
			else continue;
				

			
		}
		
	}
	
	
	// method to clear array
	static int[] clearAry(int[] ary) {
		
		for(int i = 0; i < ary.length; i++) {
			ary[i] = 0;
		}
		
		return ary;
		
	}
	
	static void factorize(ArrayList<BigInteger> factorBase, BigInteger n, BufferedWriter outFile) throws IOException {
		
		// if n is less than 0, first vector element is 1
		if(n.compareTo(zero) == -1)
			outFile.write("1" + " ");
		else
			outFile.write("0" + " ");
	
		for(int i = 0; i < factorBase.size(); i++) {
			
			BigInteger factor = factorBase.get(i);
			
			if(n.mod(factor).equals(zero)) {
				
				int count = 0;
				
				while(n.mod(factor).equals(zero)) {
					n = n.divide(factor);
					count++;
				}
				
				outFile.write(count%2 + " ");
				
			}
			else {
				outFile.write("0" + " ");
			}
			
		}
		
		outFile.write("\n\n");
	
	}
	
	static BigInteger smoothNumber(ArrayList<BigInteger> factorBase, BigInteger n) {
		
		for(int i = 0; i < factorBase.size(); i++) {
			
			BigInteger factor = factorBase.get(i);
			
			if(n.mod(factor).equals(zero)) {
				
				while(n.mod(factor).equals(zero))
					n = n.divide(factor);
				
			}
			
		}
		
		return n;
		
	}
	
	static int[] findPrimeFactorization(ArrayList<BigInteger> factorBase, BigInteger n){
		
		int[] factors = new int[factorBase.size()];
		
		for(int i = 0; i < factorBase.size(); i++) {
			
			BigInteger factor = factorBase.get(i);
			
			if(n.mod(factor).equals(zero)) {
				
				factors[i]++;
				
				n = n.divide(factorBase.get(i));
				
			}
			
			
		}
		
		return factors;
		
	}
	
	
	
	
	public static void main(String[] args) throws IOException {
		
		Scanner inFile = new Scanner(new FileReader(args[0]));
		//BufferedWriter outSieve = new BufferedWriter(new FileWriter(args[1]));
		BufferedWriter outSmooth = new BufferedWriter(new FileWriter(args[1]));
		BufferedWriter smooth_factorizations = new BufferedWriter(new FileWriter(args[2]));

		
		
		BigInteger modulus = new BigInteger("8721717648951034180751989933592484457226804450832605710315649207114191");
		// 947 and 9209839122440374002906008377605580208264841025166426304451583112053 are factors of modulus ^
		
		//BigInteger factor1 = new BigInteger("9209839122440374002906008377605580208264841025166426304451583112053");
		
		BigInteger factor1 = new BigInteger("9209839122440374002906008377605580208264841025166426304451583112053");
		
		// bound = exp( (1/2) (log N log log N) ^ 1/2 ) 
		double bound = 3000000;
		BigInteger bigIntN = new BigInteger("9209839122440374002906008377605580208264841025166426304451583112053");


		
		// System.out.println(bound);
		
		// smoothness bound is 362 million as calculated above
		
		// now we need to get all primes up to bound
		// we will use the sieve of eratosthenes algorithm
		
		boolean[] primes = new boolean[(int)bound + 1];
		
		for(int i = 0; i < primes.length; i++)
			primes[i] = true;
		
		// from i = 2 to sqrt(bound)
		for(int i = 2; i < (int)Math.sqrt(bound) + 1; i++) {
			
			if(primes[i] == true) {
			
				int j = i*i;
				
				while(j < bound) {
					
					primes[j] = false;
					
					j += i;
					
				}
			
			}
			
		}
		
		
		// factor base arraylist to store primes in factor base
		// i used an arraylist to reduce space taken by an array using
		// unnecessary values like composite numbers or primes that aren't in the factor base
		ArrayList<BigInteger> factorBase = new ArrayList<BigInteger>();
		
		
		for(int i = 2; i < primes.length; i++) {
			
			if(primes[i]) {
				
				BigInteger bigIntI = new BigInteger(Integer.toString(i));
				
				if(bigIntN.modPow((bigIntI.subtract(one)).divide(two), bigIntI).equals(one))
					factorBase.add(bigIntI);
					
			}
			
		}
		
		
		
		// 2097483647
		
		int intervals = factorBase.size()*9500;

		int[] relations = new int[intervals];
		int[] relations_negative = new int[intervals];

		BigInteger x = bigIntN.sqrt().add(one);
		
		/*
		System.out.print("Factor base for " + bigIntN + ": ");
		for(int i = 0; i < factorBase.size(); i++)
			System.out.print(factorBase.get(i) + " ");
			
			*/
		
		System.out.println("\nNumber of prime factors: " + factorBase.size() + "\n");
		
		
		for(int i = 0; i < relations.length ; i++) {
				
			relations[i] = 0;
			relations_negative[i] = 0;
			
		}
			
		int smooth_count = 0;
			
		
		
		// keep track of end offset of sieving functions
		int[] count1_offset = new int[factorBase.size()];
		int[] count2_offset = new int[factorBase.size()];
		int[] count1_negative_offset = new int[factorBase.size()];
		int[] count2_negative_offset = new int[factorBase.size()];
		
		int count1 = 0;
		int count2 = 0;
		int count1_negative = 0;
		int count2_negative = 0;
		
		
		// this function calculates the sieving relations for each prime
		// i put all of these into a text file to make it quicker to run the program
		// because it would take just 5 minutes to run all this because sometimes the Tonelli-Shanks program
		// wouldn't return a square root so we had to wait for a second for it to finish. And over 100,000 primes,
		// there was definitely a little bit of waiting 
		// the for loop aftet this block of code reads what this code outputs to a text file into 4 arrays
		// and those arrays are the starting indexes for the sieving function for the first iteration
		/*
		for(int i = 0; i < factorBase.size(); i++) {
			
			System.out.println("HERE1 " + i);
			
			BigInteger p = factorBase.get(i);
			
			long start = System.nanoTime();

			BigInteger root1 = shanksTonelli(bigIntN, p, start);
			
			if(root1.equals(zero))
				continue;

			BigInteger root2 = p.subtract(root1);
			
			BigInteger sieve1 = root1.subtract(x).mod(p);
			BigInteger sieve2 = root2.subtract(x).mod(p);
			
			count1 = sieve1.intValue();
			count2 = sieve2.intValue();
			count1_negative = Math.abs(p.intValue()-count1);
			count2_negative = Math.abs(p.intValue()-count2);
			
			count1_offset[i] = count1;
			count2_offset[i] = count2;
			count1_negative_offset[i] = count1_negative;
			count2_negative_offset[i] = count2_negative;

			
		}
		*/
		
		
		for(int i = 0; i < factorBase.size(); i++) {
			
			
			if(inFile.hasNext())
				count1_offset[i] = inFile.nextInt();
			if(inFile.hasNext())
				count2_offset[i] = inFile.nextInt();
			if(inFile.hasNext())
				count1_negative_offset[i] = inFile.nextInt();
			if(inFile.hasNext())
				count2_negative_offset[i] = inFile.nextInt();

		}
		
		
		
		
		System.out.println(count1);
		
		int interval_count = 0;
		
		// we want to generate factorBase size + 1 smooth relations to guarantee a solution to the null space
		while(smooth_count < factorBase.size() + 1) {
			
			System.out.println("Smooth = " + smooth_count);
			
	
			for(int i = 0; i < factorBase.size(); i++) {
				
				// load offset from previous iteration
				count1 = count1_offset[i];
				count2 = count2_offset[i];
				count1_negative = count1_negative_offset[i];
				count2_negative = count2_negative_offset[i];
				
				// if tonelli shanks didnt return an answer, you cant sieve so next relation
				if(count1 == -1) {
					continue;
				}
				
				// while not at end of relation array
				while(count1 < relations.length && count2 < relations.length && count1_negative < relations.length && count2_negative < relations.length) {

					
						BigInteger p = factorBase.get(i);
						// log p
						int log = (int)Math.ceil(Math.log10(p.intValue()));
						
						// add log p
						relations[count1] += log;
						
						// add log p
						if(!p.equals(two))
							relations[count2] += log;
						
						// a1 + i*p
						count1 += p.intValue();
						// a2 + i*p
						count2 += p.intValue();
						
						// same for negatives
						relations_negative[count1_negative] += log;
						
						if(!p.equals(two))
							relations_negative[count2_negative] += log;
						
						count1_negative += p.intValue();
						count2_negative += p.intValue();
						
				}
				
				// save offset of relations for next iterations
				// so we know where to start sieving for the next interval
				count1_offset[i] = factorBase.get(i).intValue() - (relations.length - 1 - count1) - 1;
				count2_offset[i] = factorBase.get(i).intValue() - (relations.length - 1 - count2) - 1;
				count1_negative_offset[i] = factorBase.get(i).intValue() - (relations.length - 1 - count1_negative) - 1;
				count2_negative_offset[i] = factorBase.get(i).intValue() - (relations.length - 1 - count2_negative) - 1;
				
				
			}
					
			for(int i = 0; i < relations.length; i++) {
				
				// threshold
				int threshold = (int)Math.log10(Math.abs((i*i) - bigIntN.doubleValue())) - 20;
				
				// if index is over threshold
				if(relations[i] > threshold){
					
					// calculate sequence relation
					BigInteger bigIntI = new BigInteger(Integer.toString(i));
					BigInteger intervalsBig = new BigInteger(Integer.toString(intervals));
					BigInteger intervalCountBig = new BigInteger(Integer.toString(interval_count));
					
					bigIntI = bigIntI.add( intervalsBig.multiply(intervalCountBig) );
				
					BigInteger sequence_n = ((x.add(bigIntI)).pow(2)).subtract(bigIntN);
					
					// if its actually smooth
					if(quadratic_sieve.smoothNumber(factorBase, sequence_n).equals(one)) {
						
						// factorize it to text file
						quadratic_sieve.factorize(factorBase, sequence_n, smooth_factorizations);
					
						// increase smooth count
						smooth_count++;
						
						outSmooth.write(bigIntI + "\n");
						
					}
					
				}
				
			}
			
			//outSmooth.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
			
			
			for(int i = 0; i < relations_negative.length; i++) {
				
				//int threshold = (int)Math.log(i*i - bigIntN.intValue());
				
				int threshold = (int)Math.log10(Math.abs((i*i) - bigIntN.doubleValue())) - 20;
				
				if(relations_negative[i] > threshold){
					
					BigInteger bigIntI = new BigInteger(Integer.toString(-1*i));
					BigInteger intervalsBig = new BigInteger(Integer.toString(intervals));
					BigInteger intervalCountBig = new BigInteger(Integer.toString(interval_count));
					
					bigIntI = bigIntI.add( intervalsBig.multiply(intervalCountBig) );
				
					BigInteger sequence_n = ((x.add(bigIntI)).pow(2)).subtract(bigIntN);
					
					if(quadratic_sieve.smoothNumber(factorBase, sequence_n).abs().equals(one)) {
						
						quadratic_sieve.factorize(factorBase, sequence_n, smooth_factorizations);
					
						smooth_count++;
						
						outSmooth.write("-" + bigIntI + "\n");
						
					}
						
					
				}
				
			}
			
			// go to next interval
			interval_count++;
			
			
			// clear relation array for next interval
			for(int i = 0; i < relations.length; i++) {
				
				relations[i] = 0;
				relations_negative[i] = 0;
				
			}
			
		}
		
		outSmooth.write("\n\n\n" + smooth_count + " smooth relations");
		
		outSmooth.close();
		smooth_factorizations.close();
		//outSieve.close();
		
	}


}
