from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

def sign(m):
	pk = keys.gen_keypair(curve.secp256k1)
	public_key = pk[1]
	
	r, s = ecdsa.sign(m,sk,curve.secp256k1,openssl_sha256,False)
	r = 0
	s = 0

	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )
