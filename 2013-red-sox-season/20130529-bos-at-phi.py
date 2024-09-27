import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ PHI, 2013-05-29
# https://www.baseball-reference.com/boxes/PHI/PHI201305290.shtml
# https://www.mlb.com/gameday/red-sox-vs-phillies/2013/05/29/347536/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-29 19:07-22:15",
        "at": "Citizens Bank Park, Philadelphia, PA",
        "att": "38,831",
        "temp": "88F, Partly Cloudy",
        "wind": "15mph, Out To LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                41: "John Lackey",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                34: "David Ortiz",
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                44: "Jackie Bradley Jr.",
                # Bullpen
                40: "Andrew Bailey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [12, "3"],
                [39, "2"],
                [37, "7"],
                [7, "6"],
                [10, "5"],
                [41, "1"],
            ],
            "bench": [
                [34, "DH"],
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
                [44, "CF"],
            ],
            "bullpen": [40, 56, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Philadelphia Phillies",
            "starter": 38,
            "roster": {
                # Lineup
                2: "Ben Revere",
                28: "Kevin Frandsen",
                11: "Jimmy Rollins",
                6: "Ryan Howard",
                3: "Delmon Young",
                9: "Domonic Brown",
                31: "Erik Kratz",
                13: "Freddy Galvis",
                38: "Kyle Kendrick",
                # Starting pitcher
                38: "Kyle Kendrick",
                # Bench
                15: "John Mayberry Jr.",
                12: "Humberto Quintero",
                19: "Laynce Nix",
                7: "Michael Martinez",
                16: "César Hernández",
                # Bullpen
                58: "Jonathan Papelbon",
                47: "Jeremy Horst",
                40: "Michael Stutes",
                59: "Antonio Bastardo",
                45: "Chad Durbin",
                37: "Mike Adams",
                44: "Jonathan Pettibone",
                30: "Justin De Fratus",
                33: "Cliff Lee",
                50: "Tyler Cloyd",
                35: "Cole Hamels",
            },
            "lefties": [47, 59, 33, 35],
            "lineup": [
                [2, "8"],
                [28, "4"],
                [11, "6"],
                [6, "3"],
                [3, "9"],
                [9, "7"],
                [31, "2"],
                [13, "5"],
                [38, "1"],
            ],
            "bench": [
                [15, "CF"],
                [12, "C"],
                [19, "CF"],
                [7, "2B"],
                [16, "2B"],
            ],
            "bullpen": [58, 47, 40, 59, 45, 37, 44, 30, 33, 50, 35],
        },
        "umpires": {
            "HP": "Dale Scott",
            "1B": "Bill Miller",
            "2B": "CB Bucknor",
            "3B": "Todd Tichenor",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: PHI #38 Kyle Kendrick
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b f b f b")
t1.hit(3)
t1.advance(4, "15 SF8")

# 2. BOS #29 Daniel Nava (2 - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("F7")

# 3. BOS #15 Dustin Pedroia (2 - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("SF8", rbis=1)

# 4. BOS #12 Mike Napoli (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)

# 5. BOS #39 Jarrod Saltalamacchia (X - X - 12)
t1.new_ab()
t1.pitch_list("c s b b")
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. PHI #2  Ben Revere (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G6-3")

# 2. PHI #28 Kevin Frandsen (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G4-3")

# 3. PHI #11 Jimmy Rollins (X - X - X)
b1.new_ab()
b1.pitch_list("c b f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: PHI #38 Kyle Kendrick
t2 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
t2.new_ab()
t2.pitch_list("f b b")
t2.out("G6-3")

# 7. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("c s f b")
t2.out("G4-3")

# 8. BOS #10 Jose Iglesias (X - X - X)
t2.new_ab()
t2.pitch_list("b c f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 4. PHI #6  Ryan Howard (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.hit(4)

# 5. PHI #3  Delmon Young (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(1)
b2.thrown_out(2, "9 FC3-6", 1, 41)

# 6. PHI #9  Domonic Brown (X - X - 3)
b2.new_ab()
b2.pitch_list("b f")
b2.reach("FC3-6")
b2.advance(2, "13 SB")

# 7. PHI #31 Erik Kratz (X - X - 9)
b2.new_ab()
b2.pitch_list("s")
b2.out("F9")

# 8. PHI #13 Freddy Galvis (X - X - 9)
b2.new_ab()
b2.pitch_list("1 1 c b b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: PHI #38 Kyle Kendrick
t3 = game.new_inning()

# 9. BOS #41 John Lackey (X - X - X)
t3.new_ab()
t3.pitch_list("c c f f")
t3.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t3.new_ab()
t3.out("(F)F7")

# 2. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b f d")
t3.reach("BB")
t3.advance(3, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)
t3.thrown_out(2, "12 CS", 3, 38)

# 4. BOS #12 Mike Napoli (29 - X - 15)
t3.new_ab()
t3.pitch_list("s b")
t3.no_ab("CS")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 9. PHI #38 Kyle Kendrick (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G6-3")

# 1. PHI #2  Ben Revere (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.out("G4-3")

# 2. PHI #28 Kevin Frandsen (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(2, "11 SB")

# 3. PHI #11 Jimmy Rollins (X - X - 28)
b3.new_ab()
b3.pitch_list("b c b b b")
b3.reach("BB")

# 4. PHI #6  Ryan Howard (X - 28 - 11)
b3.new_ab()
b3.pitch_list("s b b s c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: PHI #38 Kyle Kendrick
t4 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c b f f b f")
t4.out("L7")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t4.new_ab()
t4.pitch_list("f f f f s")
t4.out("K")

# 6. BOS #37 Mike Carp (X - X - X)
t4.new_ab()
t4.pitch_list("b c f")
t4.out("G3-1")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 5. PHI #3  Delmon Young (X - X - X)
b4.new_ab()
b4.out("G1-3")

# 6. PHI #9  Domonic Brown (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.hit(4)

# 7. PHI #31 Erik Kratz (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(4)

# 8. PHI #13 Freddy Galvis (X - X - X)
b4.new_ab()
b4.pitch_list("f f b f s")
b4.out("K")

# 9. PHI #38 Kyle Kendrick (X - X - X)
b4.new_ab()
b4.pitch_list("f b")
b4.hit(1)
b4.thrown_out(2, "2 FC3-6", 3, 41)

# 1. PHI #2  Ben Revere (X - X - 38)
b4.new_ab()
b4.pitch_list("b c s")
b4.reach("FC3-6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: PHI #38 Kyle Kendrick
t5 = game.new_inning()

# 7. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b c b b b")
t5.reach("BB")
t5.advance(2, "41 SAC1-4")

# 8. BOS #10 Jose Iglesias (X - X - 7)
t5.new_ab()
t5.pitch_list("c b c s")
t5.out("K")

# 9. BOS #41 John Lackey (X - X - 7)
t5.new_ab()
t5.pitch_list("1")
t5.out("SAC1-4")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F9")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 2. PHI #28 Kevin Frandsen (X - X - X)
b5.new_ab()
b5.pitch_list("f f f b b f s")
b5.out("K")

# 3. PHI #11 Jimmy Rollins (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("F9")

# 4. PHI #6  Ryan Howard (X - X - X)
b5.new_ab()
b5.pitch_list("c s b b b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: PHI #38 Kyle Kendrick
t6 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("c f")
t6.hit(4)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b")
t6.error(3)
t6.reach("E3")
t6.advance(2, "12 BB")

# 4. BOS #12 Mike Napoli (X - X - 15)
t6.new_ab()
t6.pitch_list("b s b d t f d")
t6.reach("BB")
t6.thrown_out(2, "37 DP1-6-3", 2, 38)

# 5. BOS #39 Jarrod Saltalamacchia (X - 15 - 12)
t6.new_ab()
t6.pitch_list("c f b")
t6.out("L8")

# 6. BOS #37 Mike Carp (X - 15 - 12)
t6.new_ab()
t6.pitch_list("c f b b")
t6.out("DP1-6-3")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 5. PHI #3  Delmon Young (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
# Offensive change (PHI): Pinch-runner #15 John Mayberry Jr. replaces #3 Delmon Young
b6.offensive_substitution(5, 15, "PR")
b6.atbase("PR")
b6.advance(2, "9 SB")
b6.advance(3, "9 G6-3")

# 6. PHI #9  Domonic Brown (X - X - 3)
b6.new_ab()
b6.pitch_list("c")
b6.out("G6-3")

# 7. PHI #31 Erik Kratz (15 - X - X)
b6.new_ab()
b6.pitch_list("f b c d b f f b")
b6.reach("BB")
b6.thrown_out(2, "13 DP4-6-3", 2, 41)

# 8. PHI #13 Freddy Galvis (15 - X - 31)
b6.new_ab()
b6.pitch_list("1 b b d c f")
b6.out("DP4-6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: PHI #59 Antonio Bastardo
t7 = game.new_inning()

# Pitching change (PHI): #59 Antonio Bastardo replaces #38 Kyle Kendrick, batting 9th
t7.pitching_substitution(59)
t7.defensive_substitution(9, 59, "1")

# Defensive switch (PHI): #15 John Mayberry Jr. moves to RF
t7.defensive_switch(15, "9")

# 7. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("f b c s")
t7.out("K")

# 8. BOS #10 Jose Iglesias (X - X - X)
t7.new_ab()
t7.hit(2)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #41 John Lackey, batting 9th
t7.offensive_substitution(9, 5, "PH")

# 9. BOS #5  Jonny Gomes (X - 10 - X)
t7.new_ab()
t7.pitch_list("c")
t7.reach("HBP")
t7.thrown_out(2, "29 FC4", 3, 59)

# 1. BOS #2  Jacoby Ellsbury (X - 10 - 5)
t7.new_ab()
t7.pitch_list("b f b f f d c")
t7.out("!K")

# 2. BOS #29 Daniel Nava (X - 10 - 5)
t7.new_ab()
t7.reach("FC4")


# Bot 7th
# Pitching: BOS #30 Andrew Miller
b7 = game.new_inning()

# Pitching change (BOS): #30 Andrew Miller replaces #41 John Lackey, batting 6th
b7.pitching_substitution(30)
b7.defensive_substitution(6, 30, "1")

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
b7.defensive_switch(5, "7")

# Offensive change (PHI): Pinch-hitter #16 César Hernández replaces #59 Antonio Bastardo, batting 9th
b7.offensive_substitution(9, 16, "PH")

# 9. PHI #16 César Hernández (X - X - X)
b7.new_ab()
b7.out("F8")

# 1. PHI #2  Ben Revere (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(1)
b7.advance(2, "28 SB")
b7.advance(3, "11 BB")

# 2. PHI #28 Kevin Frandsen (X - X - 2)
b7.new_ab()
b7.pitch_list("1 1 1 b b b b")
b7.reach("BB")
b7.advance(2, "11 BB")

# 3. PHI #11 Jimmy Rollins (X - 2 - 28)
b7.new_ab()
b7.pitch_list("b b c b c f b")
b7.reach("BB")

# 4. PHI #6  Ryan Howard (2 - 28 - 11)
b7.new_ab()
b7.pitch_list("f s s")
b7.out("K")

# Pitching change (BOS): #19 Koji Uehara replaces #30 Andrew Miller, batting 6th
b7.pitching_substitution(19)
b7.defensive_substitution(6, 19, "1")

# 5. PHI #15 John Mayberry Jr. (2 - 28 - 11)
b7.new_ab()
b7.pitch_list("c d")
b7.out("P6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: PHI #37 Mike Adams
t8 = game.new_inning()

# Pitching change (PHI): #37 Mike Adams replaces #59 Antonio Bastardo, batting 2nd
t8.pitching_substitution(37)
t8.defensive_substitution(2, 37, "1")

# Defensive switch (PHI): #16 César Hernández moves to 2B
t8.defensive_switch(16, "4")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b")
t8.out("F9")

# 4. BOS #12 Mike Napoli (X - X - X)
t8.new_ab()
t8.pitch_list("c f b c")
t8.out("!K")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t8.new_ab()
t8.pitch_list("f s b c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #19 Koji Uehara
b8 = game.new_inning()

# 6. PHI #9  Domonic Brown (X - X - X)
b8.new_ab()
b8.pitch_list("s b")
b8.hit(4)

# 7. PHI #31 Erik Kratz (X - X - X)
b8.new_ab()
b8.pitch_list("b s b b f")
b8.out("F7")

# 8. PHI #13 Freddy Galvis (X - X - X)
b8.new_ab()
b8.pitch_list("b f f f f s")
b8.out("K")

# 9. PHI #16 César Hernández (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: PHI #58 Jonathan Papelbon
t9 = game.new_inning()

# Pitching change (PHI): #58 Jonathan Papelbon replaces #37 Mike Adams, batting 2nd
t9.pitching_substitution(58)
t9.defensive_substitution(2, 58, "1")

# Offensive change (BOS): Pinch-hitter #44 Jackie Bradley Jr. replaces #19 Koji Uehara, batting 6th
t9.offensive_substitution(6, 44, "PH")

# 6. BOS #44 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("c b s s")
t9.out("K")

# 7. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f b f f b")
t9.reach("BB")
t9.advance(2, "5 1B")
t9.advance(4, "2 2B")

# Offensive change (BOS): Pinch-hitter #34 David Ortiz replaces #10 Jose Iglesias, batting 8th
t9.offensive_substitution(8, 34, "PH")

# 8. BOS #34 David Ortiz (X - X - 7)
t9.new_ab()
t9.pitch_list("b")
t9.out("F9")

# 9. BOS #5  Jonny Gomes (X - X - 7)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(3, "2 2B")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 5)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(2, rbis=1)

# 2. BOS #29 Daniel Nava (5 - 2 - X)
t9.new_ab()
t9.out("G3")

# Winning team: PHI
# WP: PHI #38 Kyle Kendrick
game.winning_pitcher(38)
# SV: PHI #58 Jonathan Papelbon
game.save_pitcher(58)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
