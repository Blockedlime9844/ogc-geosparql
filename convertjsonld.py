from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import sys

g = Graph().parse(sys.argv[1], format='turtle')

#context = {"@vocab": "http://purl.org/dc/terms/", "@language": "en"}
jsonld=g.serialize(format='json-ld', indent=2,destination=sys.argv[2])
