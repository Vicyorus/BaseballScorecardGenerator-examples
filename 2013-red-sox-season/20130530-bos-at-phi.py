import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ PHI, 2013-05-30
# https://www.baseball-reference.com/boxes/PHI/PHI201305300.shtml
# https://www.mlb.com/gameday/red-sox-vs-phillies/2013/05/30/347551/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-30 19:06-22:21",
        "at": "Citizens Bank Park, Philadelphia, PA",
        "att": "40,083",
        "temp": "92F, Partly Cloudy",
        "wind": "10mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 56,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                37: "Mike Carp",
                7: "Stephen Drew",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                56: "Franklin Morales",
                # Starting pitcher
                56: "Franklin Morales",
                # Bench
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                44: "Jackie Bradley Jr.",
                12: "Mike Napoli",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
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
                [34, "3"],
                [37, "7"],
                [7, "6"],
                [39, "2"],
                [10, "5"],
                [56, "1"],
            ],
            "bench": [
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
                [44, "CF"],
                [12, "1B"],
            ],
            "bullpen": [40, 41, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "home": {
            "team": "Philadelphia Phillies",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Ben Revere",
                16: "César Hernández",
                11: "Jimmy Rollins",
                3: "Delmon Young",
                9: "Domonic Brown",
                28: "Kevin Frandsen",
                31: "Erik Kratz",
                13: "Freddy Galvis",
                44: "Jonathan Pettibone",
                # Starting pitcher
                44: "Jonathan Pettibone",
                # Bench
                6: "Ryan Howard",
                19: "Laynce Nix",
                15: "John Mayberry Jr.",
                12: "Humberto Quintero",
                7: "Michael Martinez",
                # Bullpen
                58: "Jonathan Papelbon",
                30: "Justin De Fratus",
                47: "Jeremy Horst",
                40: "Michael Stutes",
                33: "Cliff Lee",
                59: "Antonio Bastardo",
                45: "Chad Durbin",
                50: "Tyler Cloyd",
                37: "Mike Adams",
                35: "Cole Hamels",
            },
            "lefties": [47, 33, 59, 35],
            "lineup": [
                [2, "8"],
                [16, "4"],
                [11, "6"],
                [3, "9"],
                [9, "7"],
                [28, "3"],
                [31, "2"],
                [13, "5"],
                [44, "1"],
            ],
            "bench": [
                [6, "1B"],
                [19, "CF"],
                [15, "CF"],
                [12, "C"],
                [7, "2B"],
            ],
            "bullpen": [58, 30, 47, 40, 33, 59, 45, 50, 37, 35],
        },
        "umpires": {
            "HP": "Bill Miller",
            "1B": "CB Bucknor",
            "2B": "Todd Tichenor",
            "3B": "Dale Scott",
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
# Pitching: PHI #44 Jonathan Pettibone
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.advance(3, "29 1B")
t1.advance(4, "15 G4-3")

# 2. BOS #29 Daniel Nava (X - X - 2)
t1.new_ab()
t1.pitch_list("c s f")
t1.hit(1)
t1.advance(2, "15 G4-3")
t1.advance(4, "37 1B")

# 3. BOS #15 Dustin Pedroia (2 - X - 29)
t1.new_ab()
t1.pitch_list("c b d")
t1.out("G4-3", rbis=1)

# 4. BOS #34 David Ortiz (X - 29 - X)
t1.new_ab()
t1.pitch_list("b c b b b")
t1.reach("BB")
t1.advance(2, "37 1B")
t1.advance(4, "39 2B")

# 5. BOS #37 Mike Carp (X - 29 - 34)
t1.new_ab()
t1.pitch_list("c b c f b")
t1.hit(1, rbis=1)
t1.advance(4, "39 2B")

# 6. BOS #7  Stephen Drew (X - 34 - 37)
t1.new_ab()
t1.pitch_list("c c s")
t1.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - 34 - 37)
t1.new_ab()
t1.hit(2, rbis=2)

# 8. BOS #10 Jose Iglesias (X - 39 - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #56 Franklin Morales
b1 = game.new_inning()

# 1. PHI #2  Ben Revere (X - X - X)
b1.new_ab()
b1.pitch_list("c c b")
b1.out("G4-3")

# 2. PHI #16 César Hernández (X - X - X)
b1.new_ab()
b1.pitch_list("b c b c b")
b1.hit(1)
b1.advance(4, "3 HR")

# 3. PHI #11 Jimmy Rollins (X - X - 16)
b1.new_ab()
b1.pitch_list("b 1 c")
b1.out("F7")

# 4. PHI #3  Delmon Young (X - X - 16)
b1.new_ab()
b1.pitch_list("b f")
b1.hit(4, rbis=2)

# 5. PHI #9  Domonic Brown (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.hit(1)
b1.thrown_out(2, "28 CS", 3, 56)

# 6. PHI #28 Kevin Frandsen (X - X - 9)
b1.new_ab()
b1.pitch_list("1 1 b 1 s b c")
b1.no_ab("CS")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: PHI #44 Jonathan Pettibone
t2 = game.new_inning()

# 9. BOS #56 Franklin Morales (X - X - X)
t2.new_ab()
t2.pitch_list("b m s b b t")
t2.out("KT")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b b")
t2.reach("BB")
t2.advance(2, "15 SB")
t2.advance(3, "15 1B")

# 2. BOS #29 Daniel Nava (X - X - 2)
t2.new_ab()
t2.pitch_list("c")
t2.out("F8")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
t2.new_ab()
t2.pitch_list("1 c 1 b f b b")
t2.hit(1)

# 4. BOS #34 David Ortiz (2 - X - 15)
t2.new_ab()
t2.pitch_list("f")
t2.out("F8")


# Bot 2nd
# Pitching: BOS #56 Franklin Morales
b2 = game.new_inning()

# 6. PHI #28 Kevin Frandsen (X - X - X)
b2.new_ab()
b2.pitch_list("c c")
b2.out("G4-3")

# 7. PHI #31 Erik Kratz (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F8")

# 8. PHI #13 Freddy Galvis (X - X - X)
b2.new_ab()
b2.pitch_list("c c")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: PHI #44 Jonathan Pettibone
t3 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
t3.new_ab()
t3.pitch_list("c b s s")
t3.out("K")

# 6. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b b f d")
t3.reach("BB")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - 7)
t3.new_ab()
t3.pitch_list("b b c f s")
t3.out("K")

# 8. BOS #10 Jose Iglesias (X - X - 7)
t3.new_ab()
t3.pitch_list("1 c")
t3.out("L4")


# Bot 3rd
# Pitching: BOS #56 Franklin Morales
b3 = game.new_inning()

# 9. PHI #44 Jonathan Pettibone (X - X - X)
b3.new_ab()
b3.pitch_list("b b c f f b c")
b3.out("!K")

# 1. PHI #2  Ben Revere (X - X - X)
b3.new_ab()
b3.pitch_list("l b")
b3.out("L7")

# 2. PHI #16 César Hernández (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("L7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: PHI #44 Jonathan Pettibone
t4 = game.new_inning()

# 9. BOS #56 Franklin Morales (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f c")
t4.out("!K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(2, "29 SB")

# 2. BOS #29 Daniel Nava (X - X - 2)
t4.new_ab()
t4.pitch_list("b b")
t4.out("F8")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.out("F9")


# Bot 4th
# Pitching: BOS #56 Franklin Morales
b4 = game.new_inning()

# 3. PHI #11 Jimmy Rollins (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b b")
b4.reach("BB")
b4.advance(2, "9 1B")
b4.advance(3, "28 BB")

# 4. PHI #3  Delmon Young (X - X - 11)
b4.new_ab()
b4.pitch_list("1 f 1 s 1 f b f t")
b4.out("KT")

# 5. PHI #9  Domonic Brown (X - X - 11)
b4.new_ab()
b4.pitch_list("1 1 b b c")
b4.hit(1)
b4.advance(2, "28 BB")

# 6. PHI #28 Kevin Frandsen (X - 11 - 9)
b4.new_ab()
b4.pitch_list("b b b b")
b4.reach("BB")
b4.thrown_out(2, "31 DP6-4-3", 2, 56)

# 7. PHI #31 Erik Kratz (11 - 9 - 28)
b4.new_ab()
b4.pitch_list("b c b s")
b4.out("DP6-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: PHI #44 Jonathan Pettibone
t5 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b b b")
t5.reach("BB")
t5.thrown_out(2, "7 DP4-3", 2, 44)

# 5. BOS #37 Mike Carp (X - X - 34)
t5.new_ab()
t5.pitch_list("f c b f b")
t5.out("F8")

# 6. BOS #7  Stephen Drew (X - X - 34)
t5.new_ab()
t5.pitch_list("s c b")
t5.out("DP4-3")


# Bot 5th
# Pitching: BOS #56 Franklin Morales
b5 = game.new_inning()

# 8. PHI #13 Freddy Galvis (X - X - X)
b5.new_ab()
b5.pitch_list("c c f")
b5.out("P6")

# Offensive change (PHI): Pinch-hitter #7 Michael Martinez replaces #44 Jonathan Pettibone, batting 9th
b5.offensive_substitution(9, 7, "PH")

# 9. PHI #7  Michael Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c c")
b5.out("L5")

# 1. PHI #2  Ben Revere (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("L4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: PHI #47 Jeremy Horst
t6 = game.new_inning()

# Pitching change (PHI): #47 Jeremy Horst replaces #44 Jonathan Pettibone, batting 9th
t6.pitching_substitution(47)
t6.defensive_substitution(9, 47, "1")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t6.new_ab()
t6.pitch_list("f f f f s")
t6.out("K")

# 8. BOS #10 Jose Iglesias (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.hit(1)
t6.thrown_out(2, "9-6", 2, 47)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #56 Franklin Morales, batting 9th
t6.offensive_substitution(9, 5, "PH")

# 9. BOS #5  Jonny Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("s b b c f")
t6.hit(4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t6.new_ab()
t6.reach("HBP")
t6.advance(2, "29 SB")
t6.advance(3, "29 SB")

# 2. BOS #29 Daniel Nava (X - X - 2)
t6.new_ab()
t6.pitch_list("b b 2 b b")
t6.reach("BB")

# 3. BOS #15 Dustin Pedroia (2 - X - 29)
t6.new_ab()
t6.pitch_list("b")
t6.out("L8")


# Bot 6th
# Pitching: BOS #32 Craig Breslow
b6 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #56 Franklin Morales, batting 9th
b6.pitching_substitution(32)
b6.defensive_substitution(9, 32, "1")

# 2. PHI #16 César Hernández (X - X - X)
b6.new_ab()
b6.pitch_list("l")
b6.out("G5-3")

# 3. PHI #11 Jimmy Rollins (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f f f b f f")
b6.out("G5-3")

# 4. PHI #3  Delmon Young (X - X - X)
b6.new_ab()
b6.pitch_list("c f b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: PHI #47 Jeremy Horst
t7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.hit(4)

# Offensive change (BOS): Pinch-hitter #12 Mike Napoli replaces #37 Mike Carp, batting 5th
t7.offensive_substitution(5, 12, "PH")

# 5. BOS #12 Mike Napoli (X - X - X)
t7.new_ab()
t7.pitch_list("c b s")
t7.out("F8")

# 6. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("c b s b f b s")
t7.out("K")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("(F)P3")


# Bot 7th
# Pitching: BOS #32 Craig Breslow
b7 = game.new_inning()

# Defensive change (BOS): #44 Jackie Bradley Jr. replaces #34 David Ortiz (1B), playing LF, batting 4th
b7.defensive_substitution(4, 44, "7")

# Defensive switch (BOS): #12 Mike Napoli moves to 1B
b7.defensive_switch(12, "3")

# 5. PHI #9  Domonic Brown (X - X - X)
b7.new_ab()
b7.pitch_list("f f f b b f s")
b7.out("K")

# Pitching change (BOS): #59 Clayton Mortensen replaces #32 Craig Breslow, batting 9th
b7.pitching_substitution(59)
b7.defensive_substitution(9, 59, "1")

# 6. PHI #28 Kevin Frandsen (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G1-3")

# 7. PHI #31 Erik Kratz (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.reach("HBP")

# 8. PHI #13 Freddy Galvis (X - X - 31)
b7.new_ab()
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: PHI #40 Michael Stutes
t8 = game.new_inning()

# Pitching change (PHI): #40 Michael Stutes replaces #47 Jeremy Horst, batting 9th
t8.pitching_substitution(40)
t8.defensive_substitution(9, 40, "1")

# 8. BOS #10 Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("s b")
t8.out("G4-3")

# 9. BOS #5  Jonny Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("c s b s")
t8.out("K")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t8.new_ab()
t8.hit(1)
t8.error(2)
t8.advance(2, "29 SB")
t8.advance(3, "29 E2")

# 2. BOS #29 Daniel Nava (X - X - 2)
t8.new_ab()
t8.pitch_list("1 1 1 1 b c f")
t8.reach("HBP")

# 3. BOS #15 Dustin Pedroia (2 - X - 29)
t8.new_ab()
t8.pitch_list("b 1")
t8.out("L9")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #59 Clayton Mortensen, batting 9th
b8.pitching_substitution(36)
b8.defensive_substitution(9, 36, "1")

# Offensive change (PHI): Pinch-hitter #19 Laynce Nix replaces #40 Michael Stutes, batting 9th
b8.offensive_substitution(9, 19, "PH")

# 9. PHI #19 Laynce Nix (X - X - X)
b8.new_ab()
b8.pitch_list("c s f s")
b8.out("K")

# 1. PHI #2  Ben Revere (X - X - X)
b8.new_ab()
b8.pitch_list("c f b c")
b8.out("!K")

# 2. PHI #16 César Hernández (X - X - X)
b8.new_ab()
b8.pitch_list("s t f")
b8.hit(1)

# 3. PHI #11 Jimmy Rollins (X - X - 16)
b8.new_ab()
b8.pitch_list("f s f")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: PHI #45 Chad Durbin
t9 = game.new_inning()

# Pitching change (PHI): #45 Chad Durbin replaces #40 Michael Stutes, batting 9th
t9.pitching_substitution(45)
t9.defensive_substitution(9, 45, "1")

# 4. BOS #44 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.hit(1)
t9.advance(3, "12 1B")
t9.advance(4, "7 G4-3")

# 5. BOS #12 Mike Napoli (X - X - 44)
t9.new_ab()
t9.pitch_list("b f c b")
t9.hit(1)
t9.advance(2, "7 G4-3")
t9.advance(4, "39 2B")

# 6. BOS #7  Stephen Drew (44 - X - 12)
t9.new_ab()
t9.out("G4-3", rbis=1)

# 7. BOS #39 Jarrod Saltalamacchia (X - 12 - X)
t9.new_ab()
t9.pitch_list("b s b d f")
t9.hit(2, rbis=1)
t9.advance(4, "10 2B")

# 8. BOS #10 Jose Iglesias (X - 39 - X)
t9.new_ab()
t9.pitch_list("c b s f b f b f")
t9.hit(2, rbis=1)

# Offensive change (BOS): Pinch-hitter #23 Pedro Ciriaco replaces #36 Junichi Tazawa, batting 9th
t9.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Pedro Ciriaco (X - 10 - X)
t9.new_ab()
t9.pitch_list("t b f b t")
t9.out("KT")

# 1. BOS #2  Jacoby Ellsbury (X - 10 - X)
t9.new_ab()
t9.pitch_list("f f b")
t9.out("G4-3")


# Bot 9th
# Pitching: BOS #40 Andrew Bailey
b9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #36 Junichi Tazawa, batting 6th
b9.pitching_substitution(40)
b9.defensive_substitution(6, 40, "1")

# Defensive switch (BOS): #10 Jose Iglesias moves to SS
b9.defensive_switch(10, "6")

# Defensive switch (BOS): #23 Pedro Ciriaco moves to 3B
b9.defensive_switch(23, "5")

# 4. PHI #3  Delmon Young (X - X - X)
b9.new_ab()
b9.out("L8")

# 5. PHI #9  Domonic Brown (X - X - X)
b9.new_ab()
b9.pitch_list("c f b s")
b9.out("K")

# 6. PHI #28 Kevin Frandsen (X - X - X)
b9.new_ab()
b9.pitch_list("s")
b9.hit(2)

# 7. PHI #31 Erik Kratz (X - 28 - X)
b9.new_ab()
b9.pitch_list("b c b f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #56 Franklin Morales
game.winning_pitcher(56, is_away_team=True)

# Loser team: PHI
# LP: PHI #44 Jonathan Pettibone
game.losing_pitcher(44)

# print(game)
game.generate_scorecard()
