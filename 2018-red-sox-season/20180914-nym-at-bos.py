import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYM @ BOS, 2018-09-14
# https://www.baseball-reference.com/boxes/BOS/BOS201809140.shtml
# https://www.mlb.com/gameday/mets-vs-red-sox/2018/09/14/531612/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-14 19:10-22:09",
        "at": "Fenway Park, Boston, MA",
        "att": "37,117",
        "temp": "67F, Partly Cloudy",
        "wind": "6mph, In From RF",
        "away": {
            "team": "New York Mets",
            "starter": 34,
            "roster": {
                # Lineup
                1: "Amed Rosario",
                68: "Jeff McNeil",
                30: "Michael Conforto",
                19: "Jay Bruce",
                21: "Todd Frazier",
                9: "Brandon Nimmo",
                22: "Dominic Smith",
                16: "Austin Jackson",
                3: "Tomás Nido",
                # Starting pitcher
                34: "Noah Syndergaard",
                # Bench
                29: "Devin Mesoraco",
                26: "Kevin Plawecki",
                4: "Wilmer Flores",
                7: "José Reyes",
                72: "Jack Reinheimer",
                59: "Jose Lobaton",
                # Bullpen
                32: "Steven Matz",
                45: "Zack Wheeler",
                73: "Daniel Zamora",
                49: "Tyler Bashlor",
                70: "Eric Hanhold",
                63: "Tim Peterson",
                51: "Paul Sewald",
                35: "Jacob Rhame",
                55: "Corey Oswalt",
                48: "Jacob deGrom",
                62: "Drew Smith",
                47: "Drew Gagnon",
                39: "Jerry Blevins",
                65: "Robert Gsellman",
                67: "Seth Lugo",
                38: "Anthony Swarzak",
                40: "Jason Vargas",
            },
            "lefties": [32, 73, 39, 40],
            "lineup": [
                [1, "6"],
                [68, "4"],
                [30, "7"],
                [19, "3"],
                [21, "5"],
                [9, "9"],
                [22, "0"],
                [16, "8"],
                [3, "2"],
            ],
            "bench": [
                [29, "C"],
                [26, "C"],
                [4, "1B"],
                [7, "SS"],
                [72, "SS"],
                [59, "C"],
            ],
            "bullpen": [32, 45, 73, 49, 70, 63, 51, 35, 55, 48, 62, 47, 39, 65, 67, 38, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 67,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                5: "Ian Kinsler",
                19: "Jackie Bradley Jr.",
                23: "Blake Swihart",
                # Starting pitcher
                67: "William Cuevas",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                59: "Sam Travis",
                3: "Sandy León",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [5, "4"],
                [19, "8"],
                [23, "2"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [12, "2B"],
                [59, "1B"],
                [3, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 22, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Todd Tichenor",
            "1B": "Chad Whitson",
            "2B": "Bill Miller",
            "3B": "Angel Hernandez",
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
# Pitching: BOS #67 William Cuevas
t1 = game.new_inning()

# 1. NYM #1  Amed Rosario (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("L8")

# 2. NYM #68 Jeff McNeil (X - X - X)
t1.new_ab()
t1.pitch_list("b s f s")
t1.out("K")

# 3. NYM #30 Michael Conforto (X - X - X)
t1.new_ab()
t1.hit(2)
t1.advance(4, "19 2B")

# 4. NYM #19 Jay Bruce (X - 30 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.hit(2, rbis=1)

# 5. NYM #21 Todd Frazier (X - 19 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b f s b f b f b")
t1.reach("BB")

# 6. NYM #9  Brandon Nimmo (X - 19 - 21)
t1.new_ab(is_risp=True)
t1.pitch_list("b f f b")
t1.out("G4-3")


# Bot 1st
# Pitching: NYM #34 Noah Syndergaard
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b f")
b1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G4-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("b f s c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #67 William Cuevas
t2 = game.new_inning()

# 7. NYM #22 Dominic Smith (X - X - X)
t2.new_ab()
t2.pitch_list("b f s f f s")
t2.out("K")

# 8. NYM #16 Austin Jackson (X - X - X)
t2.new_ab()
t2.pitch_list("c b f c")
t2.out("!K")

# 9. NYM #3  Tomás Nido (X - X - X)
t2.new_ab()
t2.pitch_list("s s s")
t2.out("K")


# Bot 2nd
# Pitching: NYM #34 Noah Syndergaard
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f")
b2.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("c b s b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #67 William Cuevas
t3 = game.new_inning()

# 1. NYM #1  Amed Rosario (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(1)
t3.advance(2, "30 HBP")
t3.advance(4, "19 HR")

# Pitching change (BOS): #63 Robby Scott replaces #67 William Cuevas
t3.pitching_substitution(63)

# 2. NYM #68 Jeff McNeil (X - X - 1)
t3.new_ab()
t3.pitch_list("b b b c")
t3.out("F7")

# 3. NYM #30 Michael Conforto (X - X - 1)
t3.new_ab()
t3.pitch_list("b 1 b f c")
t3.reach("HBP")
t3.advance(4, "19 HR")

# 4. NYM #19 Jay Bruce (X - 1 - 30)
t3.new_ab(is_risp=True)
t3.pitch_list("f b")
t3.hit(4, rbis=3)

# 5. NYM #21 Todd Frazier (X - X - X)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "9 HBP")
t3.advance(3, "22 BB")

# 6. NYM #9  Brandon Nimmo (X - X - 21)
t3.new_ab()
t3.pitch_list("c b b")
t3.reach("HBP")
t3.advance(2, "22 BB")

# 7. NYM #22 Dominic Smith (X - 21 - 9)
t3.new_ab(is_risp=True)
t3.pitch_list("b d b b")
t3.reach("BB")
t3.thrown_out(2, "16 DP6-4-3", 2, 61)

# Pitching change (BOS): #61 Brian Johnson replaces #63 Robby Scott
t3.pitching_substitution(61)

# 8. NYM #16 Austin Jackson (21 - 9 - 22)
t3.new_ab(is_risp=True)
t3.pitch_list("s d b s b")
t3.out("DP6-4-3")


# Bot 3rd
# Pitching: NYM #34 Noah Syndergaard
b3 = game.new_inning()

# 7. BOS #5  Ian Kinsler (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f")
b3.hit(1)
b3.advance(2, "19 SB")
b3.advance(3, "16 SB")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 5)
b3.new_ab(is_risp=True)
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "16 SB")

# 9. BOS #23 Blake Swihart (X - 5 - 19)
b3.new_ab(is_risp=True)
b3.pitch_list("c c 2 s")
b3.out("K")

# 1. BOS #50 Mookie Betts (X - 5 - 19)
b3.new_ab(is_risp=True)
b3.pitch_list("c")
b3.out("F7")

# 2. BOS #16 Andrew Benintendi (X - 5 - 19)
b3.new_ab(is_risp=True)
b3.pitch_list("b b f b f")
b3.out("G4-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 9. NYM #3  Tomás Nido (X - X - X)
t4.new_ab()
t4.pitch_list("b c c s")
t4.out("K")

# 1. NYM #1  Amed Rosario (X - X - X)
t4.new_ab()
t4.pitch_list("s f b b")
t4.out("G6-3")

# 2. NYM #68 Jeff McNeil (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.hit(4)

# 3. NYM #30 Michael Conforto (X - X - X)
t4.new_ab()
t4.pitch_list("b c f b b")
t4.out("G3")


# Bot 4th
# Pitching: NYM #34 Noah Syndergaard
b4 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b f b f")
b4.out("F9")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("s s b b f")
b4.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b4.new_ab()
b4.pitch_list("1 1 b")
b4.out("P4")

# 6. BOS #11 Rafael Devers (X - X - 28)
b4.new_ab()
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 4. NYM #19 Jay Bruce (X - X - X)
t5.new_ab()
t5.pitch_list("c f b f b c")
t5.out("!K")

# 5. NYM #21 Todd Frazier (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b b")
t5.hit(1)

# 6. NYM #9  Brandon Nimmo (X - X - 21)
t5.new_ab()
t5.pitch_list("c b b d c c")
t5.out("!K")

# 7. NYM #22 Dominic Smith (X - X - 21)
t5.new_ab()
t5.out("F7")


# Bot 5th
# Pitching: NYM #34 Noah Syndergaard
b5 = game.new_inning()

# 7. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f s")
b5.out("K")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c f b s")
b5.out("K")

# 9. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c f b")
b5.reach("BB")

# 1. BOS #50 Mookie Betts (X - X - 23)
b5.new_ab()
b5.pitch_list("1 1 c b")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #61 Brian Johnson
t6 = game.new_inning()

# 8. NYM #16 Austin Jackson (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f")
t6.out("P4")

# 9. NYM #3  Tomás Nido (X - X - X)
t6.new_ab()
t6.pitch_list("f s f s")
t6.out("K")

# 1. NYM #1  Amed Rosario (X - X - X)
t6.new_ab()
t6.out("F9")


# Bot 6th
# Pitching: NYM #34 Noah Syndergaard
b6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G4-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("s b b f f")
b6.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b6.new_ab()
b6.pitch_list("b f f f b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #61 Brian Johnson
t7 = game.new_inning()

# 2. NYM #68 Jeff McNeil (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f")
t7.out("F7")

# 3. NYM #30 Michael Conforto (X - X - X)
t7.new_ab()
t7.pitch_list("b b s b b")
t7.reach("BB")
t7.thrown_out(2, "21 FC5-4", 3, 61)

# 4. NYM #19 Jay Bruce (X - X - 30)
t7.new_ab()
t7.pitch_list("f")
t7.out("F8")

# 5. NYM #21 Todd Frazier (X - X - 30)
t7.new_ab()
t7.pitch_list("c b s d")
t7.reach("FC5-4")


# Bot 7th
# Pitching: NYM #34 Noah Syndergaard
b7 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G5-3")

# 7. BOS #5  Ian Kinsler (X - X - X)
b7.new_ab()
b7.pitch_list("b b c")
b7.hit(1)
b7.thrown_out(1, "19 PO", 2, 34)

# 8. BOS #19 Jackie Bradley Jr. (X - X - 5)
b7.new_ab()
b7.pitch_list("1 f b c 1 b f")
b7.out("L4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #47 Tyler Thornburg
t8 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #61 Brian Johnson
t8.pitching_substitution(47)

# 6. NYM #9  Brandon Nimmo (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b b")
t8.reach("BB")
t8.advance(2, "16 SB")
t8.advance(4, "16 HR")

# 7. NYM #22 Dominic Smith (X - X - 9)
t8.new_ab()
t8.out("F8")

# 8. NYM #16 Austin Jackson (X - X - 9)
t8.new_ab(is_risp=True)
t8.pitch_list("b f f b b f")
t8.hit(4, rbis=2)

# 9. NYM #3  Tomás Nido (X - X - X)
t8.new_ab()
t8.pitch_list("c s")
t8.out("G5-3")

# 1. NYM #1  Amed Rosario (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.hit(4)

# Pitching change (BOS): #31 Drew Pomeranz replaces #47 Tyler Thornburg
t8.pitching_substitution(31)

# 2. NYM #68 Jeff McNeil (X - X - X)
t8.new_ab()
t8.pitch_list("b b f b f f")
t8.hit(1)

# 3. NYM #30 Michael Conforto (X - X - 68)
t8.new_ab()
t8.pitch_list("c b")
t8.out("L7")


# Bot 8th
# Pitching: NYM #39 Jerry Blevins
b8 = game.new_inning()

# Pitching change (NYM): #39 Jerry Blevins replaces #34 Noah Syndergaard
b8.pitching_substitution(39)

# 9. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("P4")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(2, "59 WP")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #16 Andrew Benintendi, batting 2nd
b8.offensive_substitution(2, 25, "PH")

# 2. BOS #25 Steve Pearce (X - X - 50)
b8.new_ab()
b8.pitch_list("c b f f")
b8.out("P3")

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #18 Mitch Moreland, batting 3rd
b8.offensive_substitution(3, 59, "PH")

# 3. BOS #59 Sam Travis (X - X - 50)
b8.new_ab(is_risp=True)
b8.pitch_list("c s b b f s")
b8.wp()
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #31 Drew Pomeranz
t9 = game.new_inning()

# Defensive switch (BOS): #25 Steve Pearce moves to LF
t9.defensive_switch(25, "7")

# Defensive switch (BOS): #59 Sam Travis moves to 1B
t9.defensive_switch(59, "3")

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #2 Xander Bogaerts (SS), playing SS, batting 5th
t9.defensive_substitution(5, 30, "6")

# 4. NYM #19 Jay Bruce (X - X - X)
t9.new_ab()
t9.out("F7")

# 5. NYM #21 Todd Frazier (X - X - X)
t9.new_ab()
t9.pitch_list("b b f c b s")
t9.out("K")

# 6. NYM #9  Brandon Nimmo (X - X - X)
t9.new_ab()
t9.pitch_list("f f c")
t9.out("!K")


# Bot 9th
# Pitching: NYM #49 Tyler Bashlor
b9 = game.new_inning()

# Pitching change (NYM): #49 Tyler Bashlor replaces #39 Jerry Blevins
b9.pitching_substitution(49)

# Defensive change (NYM): #72 Jack Reinheimer replaces #30 Michael Conforto (LF), playing LF, batting 3rd
b9.defensive_substitution(3, 72, "7")

# Offensive change (BOS): Pinch-hitter #0 Brandon Phillips replaces #28 J.D. Martinez, batting 4th
b9.offensive_substitution(4, 0, "PH")

# 4. BOS #0  Brandon Phillips (X - X - X)
b9.new_ab()
b9.pitch_list("b s s s")
b9.out("K")

# 5. BOS #30 Tzu-Wei Lin (X - X - X)
b9.new_ab()
b9.pitch_list("c f f f")
b9.out("F9")

# 6. BOS #11 Rafael Devers (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G4-3")

# Winning team: NYM
# WP: NYM #34 Noah Syndergaard
game.winning_pitcher(34, is_away_team=True)

# Loser team: BOS
# LP: BOS #67 William Cuevas
game.losing_pitcher(67)

# print(game)
game.generate_scorecard()
