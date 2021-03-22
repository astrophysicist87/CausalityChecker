# =======================================================================================
#  Makefile for hydrodynamic causality checks     Christopher Plumberg, September 8, 2015
# =======================================================================================
##
##  Environments :	MAIN	= 	main sourcefile	
##
##  Usage : 	(g)make	[all]		compile the whole project		
##			install	make all and copy binary to $INSTPATH
##			distclean	remove all binaries
##  

# Set compiler and flags
CC := g++
CFLAGS= -std=c++11 -lgsl -lgslcblas -lm

# Various directories and definitions
RM          =   rm -f
O           =   .o
LDFLAGS     =   -L/usr/local/src/gsl/2.5/lib
INCFLAGS    =   -I/usr/local/src/gsl/2.5/include
SYSTEMFILES =   $(SRCGNU)


# --------------- Files involved ------------------

ifeq "$(MAIN)" ""
MAIN		=	check_causality
endif

MAINSRC     =   src/check_causality.cpp

INC		= 	src/necessary_conditions.h src/sufficient_conditions.h

# -------------------------------------------------

TARGET		=	$(MAIN)
INSTPATH	=	..

# --------------- Pattern rules -------------------

$(TARGET):
	$(CC) $(MAINSRC) -o $(TARGET) $(CFLAGS) $(INCFLAGS)  $(LDFLAGS)

# -------------------------------------------------

.PHONY:		all distclean distclean install

all:		$(TARGET)

help:
		@grep '^##' GNUmakefile

distclean:	
		-rm $(TARGET)

install:	$(TARGET)
		cp $(TARGET) $(INSTPATH)

# --------------- Dependencies -------------------
src/check_causality.cpp:         src/necessary_conditions.h src/sufficient_conditions.h
