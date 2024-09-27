import os
from baseball_scorecard.baseball_scorecard import Scorecard

# PHI @ BOS, 2013-05-28
# https://www.baseball-reference.com/boxes/BOS/BOS201305280.shtml
# https://www.mlb.com/gameday/phillies-vs-red-sox/2013/05/28/347517/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-28 19:13-21:43",
        "at": "Fenway Park, Boston, MA",
        "att": "33,463",
        "temp": "62F, Cloudy",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Philadelphia Phillies",
            "starter": 33,
            "roster": {
                # Lineup
                2: "Ben Revere",
                10: "Michael Young",
                11: "Jimmy Rollins",
                6: "Ryan Howard",
                3: "Delmon Young",
                9: "Domonic Brown",
                15: "John Mayberry Jr.",
                13: "Freddy Galvis",
                31: "Erik Kratz",
                # Starting pitcher
                33: "Cliff Lee",
                # Bench
                19: "Laynce Nix",
                12: "Humberto Quintero",
                7: "Michael Martinez",
                28: "Kevin Frandsen",
                # Bullpen
                58: "Jonathan Papelbon",
                30: "Justin De Fratus",
                47: "Jeremy Horst",
                40: "Michael Stutes",
                59: "Antonio Bastardo",
                45: "Chad Durbin",
                50: "Tyler Cloyd",
                37: "Mike Adams",
                35: "Cole Hamels",
                44: "Jonathan Pettibone",
            },
            "lefties": [33, 47, 59, 35],
            "lineup": [
                [2, "8"],
                [10, "5"],
                [11, "6"],
                [6, "3"],
                [3, "0"],
                [9, "7"],
                [15, "9"],
                [13, "4"],
                [31, "2"],
            ],
            "bench": [
                [19, "CF"],
                [12, "C"],
                [7, "2B"],
                [28, "3B"],
            ],
            "bullpen": [58, 30, 47, 40, 59, 45, 50, 37, 35, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                5: "Jonny Gomes",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                3: "David Ross",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                22: "Felix Doubront",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [5, "7"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [3, "2"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [39, "C"],
                [37, "1B"],
                [23, "3B"],
            ],
            "bullpen": [63, 40, 41, 56, 30, 32, 31, 59, 36, 11, 19, 22],
        },
        "umpires": {
            "HP": "Todd Tichenor",
            "1B": "Dale Scott",
            "2B": "Bill Miller",
            "3B": "CB Bucknor",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. PHI #2  Ben Revere (X - X - X)
t1.new_ab()
t1.pitch_list("b c b f")
t1.out("G1-3")

# 2. PHI #10 Michael Young (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(4)

# 3. PHI #11 Jimmy Rollins (X - X - X)
t1.new_ab()
t1.out("L8")

# 4. PHI #6  Ryan Howard (X - X - X)
t1.new_ab()
t1.pitch_list("c f b b b s")
t1.out("K")


# Bot 1st
# Pitching: PHI #33 Cliff Lee
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(2, "15 SB")
b1.advance(4, "15 1B")

# 2. BOS #5  Jonny Gomes (X - X - 2)
b1.new_ab()
b1.pitch_list("b c")
b1.out("F9")

# 3. BOS #15 Dustin Pedroia (X - X - 2)
b1.new_ab()
b1.pitch_list("b c b")
b1.hit(1, rbis=1)

# 4. BOS #34 David Ortiz (X - X - 15)
b1.new_ab()
b1.pitch_list("c d b")
b1.out("P5")

# 5. BOS #12 Mike Napoli (X - X - 15)
b1.new_ab()
b1.pitch_list("c b f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. PHI #3  Delmon Young (X - X - X)
t2.new_ab()
t2.out("F9")

# 6. PHI #9  Domonic Brown (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F9")

# 7. PHI #15 John Mayberry Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("b c b f c")
t2.out("!K")


# Bot 2nd
# Pitching: PHI #33 Cliff Lee
b2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b c s c")
b2.out("!K")

# 7. BOS #3  David Ross (X - X - X)
b2.new_ab()
b2.pitch_list("c s s")
b2.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b2.new_ab()
b2.pitch_list("c f")
b2.out("P6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 8. PHI #13 Freddy Galvis (X - X - X)
t3.new_ab()
t3.pitch_list("c l b f b b b")
t3.reach("BB")
t3.thrown_out(2, "31 DP6-4-3", 1, 46)

# 9. PHI #31 Erik Kratz (X - X - 13)
t3.new_ab()
t3.pitch_list("f b 1 d")
t3.out("DP6-4-3")

# 1. PHI #2  Ben Revere (X - X - X)
t3.new_ab()
t3.pitch_list("l b b b")
t3.hit(1)
t3.advance(2, "10 SB")

# 2. PHI #10 Michael Young (X - X - 2)
t3.new_ab()
t3.pitch_list("1 b c f d b")
t3.out("G5-3")


# Bot 3rd
# Pitching: PHI #33 Cliff Lee
b3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("b f c b")
b3.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f")
b3.out("G4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 3. PHI #11 Jimmy Rollins (X - X - X)
t4.new_ab()
t4.pitch_list("c b c")
t4.out("F8")

# 4. PHI #6  Ryan Howard (X - X - X)
t4.new_ab()
t4.pitch_list("b f f s")
t4.out("K")

# 5. PHI #3  Delmon Young (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)

# 6. PHI #9  Domonic Brown (X - X - 3)
t4.new_ab()
t4.pitch_list("b f b f s")
t4.out("K")


# Bot 4th
# Pitching: PHI #33 Cliff Lee
b4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c s b b")
b4.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("F8")

# 5. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("f s b f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 7. PHI #15 John Mayberry Jr. (X - X - X)
t5.new_ab()
t5.out("P6")

# 8. PHI #13 Freddy Galvis (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F7")

# 9. PHI #31 Erik Kratz (X - X - X)
t5.new_ab()
t5.pitch_list("b c b b c d")
t5.reach("BB")

# 1. PHI #2  Ben Revere (X - X - 31)
t5.new_ab()
t5.pitch_list("f c")
t5.out("G3")


# Bot 5th
# Pitching: PHI #33 Cliff Lee
b5 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
b5.new_ab()
b5.hit(1)
b5.advance(2, "3 SAC5-3")

# 7. BOS #3  David Ross (X - X - 29)
b5.new_ab()
b5.out("SAC5-3")

# 8. BOS #7  Stephen Drew (X - 29 - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("P5")

# 9. BOS #10 Jose Iglesias (X - 29 - X)
b5.new_ab()
b5.pitch_list("c c f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 2. PHI #10 Michael Young (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b f f")
t6.out("G4-3")

# 3. PHI #11 Jimmy Rollins (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "6 1B")

# 4. PHI #6  Ryan Howard (X - X - 11)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)

# 5. PHI #3  Delmon Young (X - 11 - 6)
t6.new_ab()
t6.out("F9")

# 6. PHI #9  Domonic Brown (X - 11 - 6)
t6.new_ab()
t6.out("F9")


# Bot 6th
# Pitching: PHI #33 Cliff Lee
b6 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("G4-3")

# 2. BOS #5  Jonny Gomes (X - X - X)
b6.new_ab()
b6.out("L9")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c f f b")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #46 Ryan Dempster
t7 = game.new_inning()

# 7. PHI #15 John Mayberry Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(2, "13 SAC3-4")
t7.advance(4, "31 1B")

# 8. PHI #13 Freddy Galvis (X - X - 15)
t7.new_ab()
t7.out("SAC3-4")

# 9. PHI #31 Erik Kratz (X - 15 - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1, rbis=1)
t7.advance(2, "2 G1-3")

# 1. PHI #2  Ben Revere (X - X - 31)
t7.new_ab()
t7.pitch_list("f b")
t7.out("G1-3")

# 2. PHI #10 Michael Young (X - 31 - X)
t7.new_ab()
t7.pitch_list("b s")
t7.out("G6-3")


# Bot 7th
# Pitching: PHI #33 Cliff Lee
b7 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("c c")
b7.out("G1-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G5-3")

# 6. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("b s")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Craig Breslow
t8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
t8.pitching_substitution(32)

# 3. PHI #11 Jimmy Rollins (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c f f s")
t8.out("K")

# 4. PHI #6  Ryan Howard (X - X - X)
t8.new_ab()
t8.pitch_list("b f b c s")
t8.out("K")

# 5. PHI #3  Delmon Young (X - X - X)
t8.new_ab()
t8.out("G6-3")


# Bot 8th
# Pitching: PHI #33 Cliff Lee
b8 = game.new_inning()

# 7. BOS #3  David Ross (X - X - X)
b8.new_ab()
b8.pitch_list("f c b s")
b8.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("F8")

# 9. BOS #10 Jose Iglesias (X - X - X)
b8.new_ab()
b8.pitch_list("f f b b")
b8.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b8.new_ab()
b8.pitch_list("f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #36 Junichi Tazawa
t9 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #32 Craig Breslow
t9.pitching_substitution(36)

# 6. PHI #9  Domonic Brown (X - X - X)
t9.new_ab()
t9.hit(4)

# 7. PHI #15 John Mayberry Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("b f c f c")
t9.out("!K")

# 8. PHI #13 Freddy Galvis (X - X - X)
t9.new_ab()
t9.out("L8")

# 9. PHI #31 Erik Kratz (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "2 1B")

# 1. PHI #2  Ben Revere (X - X - 31)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)

# 2. PHI #10 Michael Young (X - 31 - 2)
t9.new_ab()
t9.pitch_list("b c c b b f t")
t9.out("KT")


# Bot 9th
# Pitching: PHI #58 Jonathan Papelbon
b9 = game.new_inning()

# Pitching change (PHI): #58 Jonathan Papelbon replaces #33 Cliff Lee
b9.pitching_substitution(58)

# 2. BOS #5  Jonny Gomes (X - X - X)
b9.new_ab()
b9.pitch_list("c b c b f s")
b9.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b9.new_ab()
b9.pitch_list("c c")
b9.out("G5-3")

# 4. BOS #34 David Ortiz (X - X - X)
b9.new_ab()
b9.pitch_list("b f s f b f")
b9.out("G6-3")

# Winning team: PHI
# WP: PHI #33 Cliff Lee
game.winning_pitcher(33, is_away_team=True)
# SV: PHI #58 Jonathan Papelbon
game.save_pitcher(58, is_away_team=True)

# Loser team: BOS
# LP: BOS #46 Ryan Dempster
game.losing_pitcher(46)

# print(game)
game.generate_scorecard()
