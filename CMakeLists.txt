cmake_minimum_required (VERSION 3.25 FATAL_ERROR)

project (
	%PROJECT_NAME%
	VERSION 0.0.1
	LANGUAGES CXX C
	DESCRIPTION "%PROJECT_DESCRIPTION%"
	HOMEPAGE_URL "%PROJECT_URL%")

add_subdirectory (linfra)

limes_default_project_options ()
