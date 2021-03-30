"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str
import math


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, name, diameter, hazardous):
        """Create a new `NearEarthObject`.

        :param str designation: The primary designation for this NearEarthObject
        :param str name: The IAU name for this NearEarthObject
        :param float diameter: The diameter, in kilometers, of this NearEarthObject
        :hazardous bool: Whether or not this NearEarthObject is potentially hazardous
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        if designation == "":
            raise NameError("value of 'designation' should never be empty")
        else:
            self._designation = designation

        if name == "":
            self._name=None
        else:
            self._name = name

        if diameter == "":
            self._diameter = float("nan")
        else:
            self._diameter = float(diameter)

        if hazardous == "Y":
            self._hazardous = True
        elif hazardous == "N":
            self._hazardous = False
        else:
            self._hazardous= False
            #noticed that in some records value is missing.
            #raise NameError("Error: Wrong value of hazardous")

        # Create an empty initial collection of linked approaches.
        self._approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        #In the above, {fullname} is either {designation} ({name}) if the name exists or simply {designation} otherwise. As a hint, this is a great opportunity for a property named fullname!
        # TODO: Use self.designation and self.name to build a fullname for this object.
        if self.name!=None:
            return f'{self.designation} ({self.name})'
        else:
            return f'{self.designation}'

    @property
    def designation(self):
        return self._designation

    @property
    def name(self):
        return self._name

    @property
    def diameter(self):
        return self._diameter

    @property
    def hazardous(self):
        return self._hazardous

    @property
    def approaches(self):
        return self._approaches

    @approaches.setter
    def approaches(self,approaches_set):
        self._approaches=approaches_set

    def serialize(self):
        #{'designation': '433', 'name': 'Eros', 'diameter_km': 16.84, 'potentially_hazardous': False}
        if self.name == None:
            f_name=''
        else:
            f_name=self.name
        res_dict={'designation':self.designation, 'name':f_name, 'diameter_km':self.diameter, 'hazardous':self.hazardous}
        #row=f'row: designation:{result.designation}, name:{f_name}, diameter_km{result.neo.diameter}, hazardous:{result.neo.hazardous}'
        return res_dict

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        diameter_str=''
        condition=''
        and_str=''

        if self.hazardous == True:
            condition=' is potentially hazardous.'
        elif self.hazardous == False:
            condition=' is not potentially hazardous.'
        else:
            condition=" do not know if it's potentionally hazardous or not"

        if not math.isnan(self.diameter):
            diameter_str=f' has a diameter of {self.diameter:.3f} km'
        else:
            diameter_str=''

        if diameter_str != '' and condition != '':
            and_str=' and'
        else:
            and_str=''

        return f"A neo {self.fullname}{diameter_str}{and_str}{condition}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, time=None, distance=0.0, velocity=0.0):
        """Create a new `CloseApproach`.

        :param time: The date and time, in UTC, at which the NEO passes closest to Earth.
        :param distance: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
        :param velocity: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
        :param neo: The NearEarthObject that is making a close approach to Earth
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.

        if designation == "":
            raise NameError("Error: Wrong value of designation")
        else:
            self._designation = designation

        if velocity == "":
            raise NameError("Error: Wrong value of velocity")
        else:
            self._velocity = float(velocity)

        if time == "":
            raise NameError("Error: Wrong value of time")
        else:
            self._time = cd_to_datetime(time)  # TODO: Use the cd_to_datetime function for this attribute.

        if distance == "":
            raise NameError("Error: Wrong value of distance")
        else:
            self._distance = float(distance)


        # Create an attribute for the referenced NEO, originally None.
        self._neo = None

    @property
    def designation(self):
        return self._designation

    @property
    def time(self):
        return self._time

    @property
    def distance(self):
        return self._distance

    @property
    def velocity(self):
        return self._velocity

    @property
    def neo(self):
        return self._neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        return datetime_to_str(self.time)

    @neo.setter
    def neo(self,neo):
        self._neo = neo

    def serialize(self):
        #{'datetime_utc': '2025-11-30 02:18', 'distance_au': 0.397647483265833, 'velocity_km_s': 3.72885069167641}
        #row=f'row:datetime:{result.time_str},distance_au:{result.distance}, velocity_km_s:{result.velocity}, designation:{result.designation}, name:{f_name}, diameter_km{result.neo.diameter}, hazardous:{result.neo.hazardous}'
        res_dict={'datetime_utc':self.time_str, 'distance_au':self.distance, 'velocity_km_s':self.velocity, 'neo':self.neo.serialize()}
        #row=f'row: designation:{result.designation}, name:{f_name}, diameter_km{result.neo.diameter}, hazardous:{result.neo.hazardous}'
        return res_dict


    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.

        #On 1910-05-20 12:49, '1P (Halley)' approaches Earth at a distance of 0.15 au and a velocity of 70.56 km/s.
        if self.neo == None:
            neo_fullname = ""
        else:
            neo_fullname = self.neo.fullname
        return f"At {self.time_str}, '{neo_fullname}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
