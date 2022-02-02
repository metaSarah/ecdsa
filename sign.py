from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

def sign(m):
	sk, pk = keys.gen_keypair(curve.secp256k1)
	public_key = pk

	sig = ecdsa.sign(m, sk, curve=secp256k1, hashfunc=sha256)
	r = sig[0]
	s = sig[1]

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )
