import os
from baseball_scorecard.baseball_scorecard import Scorecard

# PHI @ BOS, 2013-05-27
# https://www.baseball-reference.com/boxes/BOS/BOS201305270.shtml
# https://www.mlb.com/gameday/phillies-vs-red-sox/2013/05/27/347501/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-05-27 19:12-22:38",
        "at": "Fenway Park, Boston, MA",
        "att": "33,627",
        "temp": "74F, Clear",
        "wind": "12mph, L To R",
        "away": {
            "team": "Philadelphia Phillies",
            "starter": 50,
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
                50: "Tyler Cloyd",
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
                33: "Cliff Lee",
                59: "Antonio Bastardo",
                45: "Chad Durbin",
                37: "Mike Adams",
                35: "Cole Hamels",
                44: "Jonathan Pettibone",
            },
            "lefties": [47, 33, 59, 35],
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
            "bullpen": [58, 30, 47, 40, 33, 59, 45, 37, 35, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 91,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                7: "Stephen Drew",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                10: "Jose Iglesias",
                # Starting pitcher
                91: "Alfredo Aceves",
                # Bench
                5: "Jonny Gomes",
                3: "David Ross",
                23: "Pedro Ciriaco",
                # Bullpen
                63: "Alex Wilson",
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
            "lefties": [30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [7, "6"],
                [37, "7"],
                [39, "2"],
                [10, "5"],
            ],
            "bench": [
                [5, "LF"],
                [3, "C"],
                [23, "3B"],
            ],
            "bullpen": [63, 40, 41, 30, 32, 31, 59, 36, 11, 19, 22, 46],
        },
        "umpires": {
            "HP": "CB Bucknor",
            "1B": "Todd Tichenor",
            "2B": "Dale Scott",
            "3B": "Bill Miller",
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
# Pitching: BOS #91 Alfredo Aceves
t1 = game.new_inning()

# 1. PHI #2  Ben Revere (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")

# 2. PHI #10 Michael Young (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.out("G1-3")

# 3. PHI #11 Jimmy Rollins (X - X - X)
t1.new_ab()
t1.pitch_list("b b f s b f f")
t1.hit(2)

# 4. PHI #6  Ryan Howard (X - 11 - X)
t1.new_ab()
t1.pitch_list("b f s s")
t1.out("K")


# Bot 1st
# Pitching: PHI #50 Tyler Cloyd
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.hit(1)
b1.advance(2, "29 G1-3")
b1.advance(3, "15 WP")
b1.advance(4, "15 HR")

# 2. BOS #29 Daniel Nava (X - X - 2)
b1.new_ab()
b1.pitch_list("b c f d")
b1.out("G1-3")

# 3. BOS #15 Dustin Pedroia (X - 2 - X)
b1.new_ab()
b1.pitch_list("b f b")
b1.wp()
b1.hit(4, rbis=2)

# 4. BOS #34 David Ortiz (X - X - X)
b1.new_ab()
b1.pitch_list("b s c s")
b1.out("K")

# 5. BOS #12 Mike Napoli (X - X - X)
b1.new_ab()
b1.hit(4)

# 6. BOS #7  Stephen Drew (X - X - X)
b1.new_ab()
b1.pitch_list("b b s b b")
b1.reach("BB")

# 7. BOS #37 Mike Carp (X - X - 7)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #91 Alfredo Aceves
t2 = game.new_inning()

# 5. PHI #3  Delmon Young (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b c")
t2.out("G6-3")

# 6. PHI #9  Domonic Brown (X - X - X)
t2.new_ab()
t2.pitch_list("b f b")
t2.error(1)
t2.reach("E1")
t2.thrown_out(2, "15 DP4-6-3", 2, 91)

# 7. PHI #15 John Mayberry Jr. (X - X - 9)
t2.new_ab()
t2.pitch_list("s")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: PHI #50 Tyler Cloyd
b2 = game.new_inning()

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("b f b c")
b2.out("F7")

# 9. BOS #10 Jose Iglesias (X - X - X)
b2.new_ab()
b2.pitch_list("c b c b b")
b2.hit(1)
b2.advance(3, "2 2B")

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b2.new_ab()
b2.pitch_list("f")
b2.hit(2)

# 2. BOS #29 Daniel Nava (10 - 2 - X)
b2.new_ab()
b2.pitch_list("f b b b c")
b2.out("L7")

# 3. BOS #15 Dustin Pedroia (10 - 2 - X)
b2.new_ab()
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #91 Alfredo Aceves
t3 = game.new_inning()

# 8. PHI #13 Freddy Galvis (X - X - X)
t3.new_ab()
t3.pitch_list("c f s")
t3.out("K")

# 9. PHI #31 Erik Kratz (X - X - X)
t3.new_ab()
t3.hit(4)

# 1. PHI #2  Ben Revere (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c b")
t3.reach("BB")
t3.thrown_out(1, "10 DP8-3", 3, 91)

# 2. PHI #10 Michael Young (X - X - 2)
t3.new_ab()
t3.pitch_list("b")
t3.out("DP8-3")


# Bot 3rd
# Pitching: PHI #50 Tyler Cloyd
b3 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(2)
b3.advance(4, "12 2B")

# 5. BOS #12 Mike Napoli (X - 34 - X)
b3.new_ab()
b3.pitch_list("f f f d")
b3.hit(2, rbis=1)
b3.advance(4, "7 1B")

# 6. BOS #7  Stephen Drew (X - 12 - X)
b3.new_ab()
b3.pitch_list("c b b s f")
b3.hit(1, rbis=1)
b3.advance(2, "39 1B")
b3.advance(4, "2 2B")

# 7. BOS #37 Mike Carp (X - X - 7)
b3.new_ab()
b3.pitch_list("s b s b f c")
b3.out("!K")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - 7)
b3.new_ab()
b3.hit(1)
b3.advance(3, "2 2B")
b3.thrown_out(4, "2 7-6-2", 3, 40)

# Pitching change (PHI): #40 Michael Stutes replaces #50 Tyler Cloyd
b3.pitching_substitution(40)

# 9. BOS #10 Jose Iglesias (X - 7 - 39)
b3.new_ab()
b3.pitch_list("b c b c f")
b3.out("P3")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - 39)
b3.new_ab()
b3.pitch_list("b b c")
b3.hit(2, rbis=1)


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #91 Alfredo Aceves
t4 = game.new_inning()

# 3. PHI #11 Jimmy Rollins (X - X - X)
t4.new_ab()
t4.pitch_list("c f b")
t4.hit(1)
t4.thrown_out(2, "6 DP4-6-3", 1, 91)

# 4. PHI #6  Ryan Howard (X - X - 11)
t4.new_ab()
t4.pitch_list("c")
t4.out("DP4-6-3")

# 5. PHI #3  Delmon Young (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)

# 6. PHI #9  Domonic Brown (X - X - 3)
t4.new_ab()
t4.pitch_list("b f t f")
t4.out("P4")


# Bot 4th
# Pitching: PHI #40 Michael Stutes
b4 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G3-1")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G4-3")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #91 Alfredo Aceves
t5 = game.new_inning()

# 7. PHI #15 John Mayberry Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.hit(1)
t5.advance(3, "2 1B")

# 8. PHI #13 Freddy Galvis (X - X - 15)
t5.new_ab()
t5.out("F7")

# 9. PHI #31 Erik Kratz (X - X - 15)
t5.new_ab()
t5.pitch_list("b c s s")
t5.out("K")

# 1. PHI #2  Ben Revere (X - X - 15)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)

# 2. PHI #10 Michael Young (15 - X - 2)
t5.new_ab()
t5.out("L1")


# Bot 5th
# Pitching: PHI #40 Michael Stutes
b5 = game.new_inning()

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("s b c s")
b5.out("K")

# 6. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("f c b")
b5.hit(1)
b5.advance(3, "37 2B")
b5.advance(4, "39 1B")

# 7. BOS #37 Mike Carp (X - X - 7)
b5.new_ab()
b5.pitch_list("1 b 1")
b5.hit(2)
b5.error(9)
b5.advance("U", "39 E9")

# 8. BOS #39 Jarrod Saltalamacchia (7 - 37 - X)
b5.new_ab()
b5.pitch_list("b b f")
b5.hit(1, rbis=1)

# 9. BOS #10 Jose Iglesias (X - X - 39)
b5.new_ab()
b5.pitch_list("d 1 c c 1 s")
b5.out("K")

# Pitching change (PHI): #47 Jeremy Horst replaces #40 Michael Stutes
b5.pitching_substitution(47)

# 1. BOS #2  Jacoby Ellsbury (X - X - 39)
b5.new_ab()
b5.pitch_list("c b c f f")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #91 Alfredo Aceves
t6 = game.new_inning()

# 3. PHI #11 Jimmy Rollins (X - X - X)
t6.new_ab()
t6.pitch_list("b s b f b b")
t6.reach("BB")
t6.advance(3, "6 1B")

# 4. PHI #6  Ryan Howard (X - X - 11)
t6.new_ab()
t6.pitch_list("f b b b s")
t6.hit(1)
t6.advance(2, "15 BB")

# 5. PHI #3  Delmon Young (11 - X - 6)
t6.new_ab()
t6.pitch_list("f s s")
t6.out("K")

# 6. PHI #9  Domonic Brown (11 - X - 6)
t6.new_ab()
t6.pitch_list("d b")
t6.out("(F)P5")

# 7. PHI #15 John Mayberry Jr. (11 - X - 6)
t6.new_ab()
t6.pitch_list("f b c d f b b")
t6.reach("BB")

# 8. PHI #13 Freddy Galvis (11 - 6 - 15)
t6.new_ab()
t6.pitch_list("b f b")
t6.out("L8")


# Bot 6th
# Pitching: PHI #47 Jeremy Horst
b6 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b f b b f f f s")
b6.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b b f f b")
b6.reach("BB")
# Offensive change (BOS): Pinch-runner #23 Pedro Ciriaco replaces #15 Dustin Pedroia
b6.offensive_substitution(3, 23, "PR")
b6.atbase("PR")
b6.advance(2, "34 1B")

# 4. BOS #34 David Ortiz (X - X - 15)
b6.new_ab()
b6.pitch_list("f b b")
b6.hit(1)

# 5. BOS #12 Mike Napoli (X - 23 - 34)
b6.new_ab()
b6.pitch_list("c b b c c")
b6.out("!K")

# 6. BOS #7  Stephen Drew (X - 23 - 34)
b6.new_ab()
b6.pitch_list("t b c c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #59 Clayton Mortensen
t7 = game.new_inning()

# Pitching change (BOS): #59 Clayton Mortensen replaces #91 Alfredo Aceves
t7.pitching_substitution(59)

# Defensive switch (BOS): #23 Pedro Ciriaco moves to 2B
t7.defensive_switch(23, "4")

# 9. PHI #31 Erik Kratz (X - X - X)
t7.new_ab()
t7.pitch_list("b f f f b b b")
t7.reach("BB")

# 1. PHI #2  Ben Revere (X - X - 31)
t7.new_ab()
t7.pitch_list("c b")
t7.out("L8")

# 2. PHI #10 Michael Young (X - X - 31)
t7.new_ab()
t7.pitch_list("s b c b b")
t7.out("L4")

# 3. PHI #11 Jimmy Rollins (X - X - 31)
t7.new_ab()
t7.pitch_list("b b c d f f")
t7.out("G4-3")


# Bot 7th
# Pitching: PHI #59 Antonio Bastardo
b7 = game.new_inning()

# Pitching change (PHI): #59 Antonio Bastardo replaces #47 Jeremy Horst
b7.pitching_substitution(59)

# 7. BOS #37 Mike Carp (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("(F)P2")

# 8. BOS #39 Jarrod Saltalamacchia (X - X - X)
b7.new_ab()
b7.out("F7")

# 9. BOS #10 Jose Iglesias (X - X - X)
b7.new_ab()
b7.pitch_list("c b f")
b7.out("P4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #59 Clayton Mortensen
t8 = game.new_inning()

# 4. PHI #6  Ryan Howard (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b f f f f")
t8.hit(2)
t8.thrown_out(3, "3 FC6-4", 1, 59)

# 5. PHI #3  Delmon Young (X - 6 - X)
t8.new_ab()
t8.pitch_list("s b")
t8.reach("FC6-4")
t8.advance(4, "9 HR")

# Pitching change (BOS): #30 Andrew Miller replaces #59 Clayton Mortensen
t8.pitching_substitution(30)

# 6. PHI #9  Domonic Brown (X - X - 3)
t8.new_ab()
t8.pitch_list("b b f f")
t8.hit(4, rbis=2)

# 7. PHI #15 John Mayberry Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("c c b")
t8.hit(1)
t8.thrown_out(2, "13 FC5-4", 2, 30)

# 8. PHI #13 Freddy Galvis (X - X - 15)
t8.new_ab()
t8.pitch_list("f c")
t8.reach("FC5-4")

# 9. PHI #31 Erik Kratz (X - X - 13)
t8.new_ab()
t8.pitch_list("c s f f d s")
t8.out("K")


# Bot 8th
# Pitching: PHI #37 Mike Adams
b8 = game.new_inning()

# Pitching change (PHI): #37 Mike Adams replaces #59 Antonio Bastardo
b8.pitching_substitution(37)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("b b c b c")
b8.out("G3")

# 2. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c f f s")
b8.out("K")

# 3. BOS #23 Pedro Ciriaco (X - X - X)
b8.new_ab()
b8.pitch_list("s")
b8.hit(1)
b8.advance(2, "34 BB")
b8.advance(3, "12 BB")
b8.advance(4, "7 BB")

# 4. BOS #34 David Ortiz (X - X - 23)
b8.new_ab()
b8.pitch_list("b b b c b")
b8.reach("BB")
b8.advance(2, "12 BB")
b8.advance(3, "7 BB")

# 5. BOS #12 Mike Napoli (X - 23 - 34)
b8.new_ab()
b8.pitch_list("s b b b c b")
b8.reach("BB")
b8.advance(2, "7 BB")

# 6. BOS #7  Stephen Drew (23 - 34 - 12)
b8.new_ab()
b8.pitch_list("c b s b f b b")
b8.reach("BB", rbis=1)
b8.thrown_out(2, "37 FC4-6", 3, 30)

# Pitching change (PHI): #30 Justin De Fratus replaces #37 Mike Adams
b8.pitching_substitution(30)

# 7. BOS #37 Mike Carp (34 - 12 - 7)
b8.new_ab()
b8.pitch_list("f")
b8.reach("FC4-6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #30 Andrew Miller
t9 = game.new_inning()

# 1. PHI #2  Ben Revere (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c f")
t9.hit(1)

# 2. PHI #10 Michael Young (X - X - 2)
t9.new_ab()
t9.pitch_list("b b f")
t9.out("F8")

# 3. PHI #11 Jimmy Rollins (X - X - 2)
t9.new_ab()
t9.pitch_list("f f f s")
t9.out("K")

# 4. PHI #6  Ryan Howard (X - X - 2)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# Winning team: BOS
# WP: BOS #91 Alfredo Aceves
game.winning_pitcher(91)

# Loser team: PHI
# LP: PHI #50 Tyler Cloyd
game.losing_pitcher(50, is_away_team=True)

# print(game)
game.generate_scorecard()
