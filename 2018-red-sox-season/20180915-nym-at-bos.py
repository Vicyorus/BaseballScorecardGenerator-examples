import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYM @ BOS, 2018-09-15
# https://www.baseball-reference.com/boxes/BOS/BOS201809150.shtml
# https://www.mlb.com/gameday/mets-vs-red-sox/2018/09/15/531627/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-15 16:06-19:17",
        "at": "Fenway Park, Boston, MA",
        "att": "36,611",
        "temp": "72F, Partly Cloudy",
        "wind": "9mph, In From RF",
        "away": {
            "team": "New York Mets",
            "starter": 55,
            "roster": {
                # Lineup
                1: "Amed Rosario",
                68: "Jeff McNeil",
                30: "Michael Conforto",
                19: "Jay Bruce",
                21: "Todd Frazier",
                9: "Brandon Nimmo",
                22: "Dominic Smith",
                26: "Kevin Plawecki",
                16: "Austin Jackson",
                # Starting pitcher
                55: "Corey Oswalt",
                # Bench
                3: "Tomás Nido",
                29: "Devin Mesoraco",
                4: "Wilmer Flores",
                7: "José Reyes",
                72: "Jack Reinheimer",
                59: "Jose Lobaton",
                # Bullpen
                32: "Steven Matz",
                45: "Zack Wheeler",
                34: "Noah Syndergaard",
                73: "Daniel Zamora",
                49: "Tyler Bashlor",
                70: "Eric Hanhold",
                63: "Tim Peterson",
                51: "Paul Sewald",
                35: "Jacob Rhame",
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
                [19, "0"],
                [21, "5"],
                [9, "9"],
                [22, "3"],
                [26, "2"],
                [16, "8"],
            ],
            "bench": [
                [3, "C"],
                [29, "C"],
                [4, "1B"],
                [7, "SS"],
                [72, "SS"],
                [59, "C"],
            ],
            "bullpen": [32, 45, 34, 73, 49, 70, 63, 51, 35, 48, 62, 47, 39, 65, 67, 38, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                5: "Ian Kinsler",
                19: "Jackie Bradley Jr.",
                11: "Rafael Devers",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                30: "Tzu-Wei Lin",
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                12: "Brock Holt",
                59: "Sam Travis",
                23: "Blake Swihart",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
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
                [28, "0"],
                [2, "6"],
                [25, "3"],
                [5, "4"],
                [19, "8"],
                [11, "5"],
                [3, "2"],
            ],
            "bench": [
                [30, "OF"],
                [36, "SS"],
                [18, "1B"],
                [12, "2B"],
                [59, "1B"],
                [23, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Chad Whitson",
            "1B": "Bill Miller",
            "2B": "Angel Hernandez",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. NYM #1  Amed Rosario (X - X - X)
t1.new_ab()
t1.out("L4")

# 2. NYM #68 Jeff McNeil (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G4-3")

# 3. NYM #30 Michael Conforto (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f b f")
t1.out("L4")


# Bot 1st
# Pitching: NYM #55 Corey Oswalt
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.reach("HBP")
b1.error(3)
b1.advance(2, "16 FC3")
b1.advance(3, "16 E3")
b1.advance("U", "2 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("b b")
b1.reach("FC3")
b1.advance(3, "2 1B")

# 3. BOS #28 J.D. Martinez (50 - X - 16)
b1.new_ab()
b1.pitch_list("s s s")
b1.out("K")

# 4. BOS #2  Xander Bogaerts (50 - X - 16)
b1.new_ab()
b1.pitch_list("b c b s 1 f 1 f")
b1.hit(1, rbis=1)
b1.advance(2, "5 SB")

# 5. BOS #25 Steve Pearce (16 - X - 2)
b1.new_ab()
b1.pitch_list("c d b")
b1.out("P4")

# 6. BOS #5  Ian Kinsler (16 - X - 2)
b1.new_ab()
b1.pitch_list("b b c b d")
b1.reach("BB")

# 7. BOS #19 Jackie Bradley Jr. (16 - 2 - 5)
b1.new_ab()
b1.pitch_list("b s")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. NYM #19 Jay Bruce (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b f b f")
t2.out("G3")

# 5. NYM #21 Todd Frazier (X - X - X)
t2.new_ab()
t2.pitch_list("f b")
t2.out("F7")

# 6. NYM #9  Brandon Nimmo (X - X - X)
t2.new_ab()
t2.reach("HBP")

# 7. NYM #22 Dominic Smith (X - X - 9)
t2.new_ab()
t2.pitch_list("b c f s")
t2.out("K")


# Bot 2nd
# Pitching: NYM #55 Corey Oswalt
b2 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.error(3)
b2.reach("E3")
b2.advance(3, "16 1B")

# 9. BOS #3  Sandy León (X - X - 11)
b2.new_ab()
b2.pitch_list("b b c 1 1")
b2.out("P6")

# 1. BOS #50 Mookie Betts (X - X - 11)
b2.new_ab()
b2.pitch_list("c c t")
b2.out("KT")

# 2. BOS #16 Andrew Benintendi (X - X - 11)
b2.new_ab()
b2.pitch_list("b b c l f b")
b2.hit(1)

# 3. BOS #28 J.D. Martinez (11 - X - 16)
b2.new_ab()
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 8. NYM #26 Kevin Plawecki (X - X - X)
t3.new_ab()
t3.pitch_list("c b s f b")
t3.out("F8")

# 9. NYM #16 Austin Jackson (X - X - X)
t3.new_ab()
t3.pitch_list("c b c b f f c")
t3.out("!K")

# 1. NYM #1  Amed Rosario (X - X - X)
t3.new_ab()
t3.pitch_list("c b c c")
t3.out("!K")


# Bot 3rd
# Pitching: NYM #55 Corey Oswalt
b3 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("c f c")
b3.out("!K")

# 5. BOS #25 Steve Pearce (X - X - X)
b3.new_ab()
b3.pitch_list("f b c b")
b3.hit(1)

# 6. BOS #5  Ian Kinsler (X - X - 25)
b3.new_ab()
b3.pitch_list("b b f f b f 1 1 f 1")
b3.out("(F)P2")

# Pitching change (NYM): #73 Daniel Zamora replaces #55 Corey Oswalt
b3.pitching_substitution(73)

# 7. BOS #19 Jackie Bradley Jr. (X - X - 25)
b3.new_ab()
b3.pitch_list("f b s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 2. NYM #68 Jeff McNeil (X - X - X)
t4.new_ab()
t4.pitch_list("b b c t b f f")
t4.hit(1)
t4.advance(2, "19 SB")
t4.advance(4, "9 HR")

# 3. NYM #30 Michael Conforto (X - X - 68)
t4.new_ab()
t4.pitch_list("c f b f f")
t4.out("L5")

# 4. NYM #19 Jay Bruce (X - X - 68)
t4.new_ab()
t4.pitch_list("c f s")
t4.out("K")

# 5. NYM #21 Todd Frazier (X - 68 - X)
t4.new_ab()
t4.pitch_list("b b s f f f f b b")
t4.reach("BB")
t4.advance(4, "9 HR")

# 6. NYM #9  Brandon Nimmo (X - 68 - 21)
t4.new_ab()
t4.pitch_list("f f f b")
t4.hit(4, rbis=3)

# 7. NYM #22 Dominic Smith (X - X - X)
t4.new_ab()
t4.pitch_list("b f s")
t4.out("F8")


# Bot 4th
# Pitching: NYM #73 Daniel Zamora
b4 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b c s b b s")
b4.out("K")

# 9. BOS #3  Sandy León (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f b c")
b4.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("b c c b f f b b")
b4.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b4.new_ab()
b4.pitch_list("1 b b c f 1 s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 8. NYM #26 Kevin Plawecki (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G3-1")

# 9. NYM #16 Austin Jackson (X - X - X)
t5.new_ab()
t5.pitch_list("c b s b s")
t5.out("K")

# 1. NYM #1  Amed Rosario (X - X - X)
t5.new_ab()
t5.pitch_list("c f")
t5.out("F9")


# Bot 5th
# Pitching: NYM #51 Paul Sewald
b5 = game.new_inning()

# Pitching change (NYM): #51 Paul Sewald replaces #73 Daniel Zamora
b5.pitching_substitution(51)

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("c b b t c")
b5.out("!K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c b f")
b5.out("P4")

# 5. BOS #25 Steve Pearce (X - X - X)
b5.new_ab()
b5.pitch_list("s b b c b")
b5.hit(1)
b5.advance(2, "5 1B")
b5.advance(4, "19 2B")

# 6. BOS #5  Ian Kinsler (X - X - 25)
b5.new_ab()
b5.pitch_list("b f 1 s")
b5.hit(1)
b5.advance(4, "19 2B")

# 7. BOS #19 Jackie Bradley Jr. (X - 25 - 5)
b5.new_ab()
b5.pitch_list("c b d")
b5.hit(2, rbis=2)
b5.advance(4, "12 2B")

# 8. BOS #11 Rafael Devers (X - 19 - X)
b5.new_ab()
b5.pitch_list("v v v v")
b5.reach("IBB")
b5.advance(4, "12 2B")

# Pitching change (NYM): #62 Drew Smith replaces #51 Paul Sewald
b5.pitching_substitution(62)

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #3 Sandy León, batting 9th
b5.offensive_substitution(9, 12, "PH")

# 9. BOS #12 Brock Holt (X - 19 - 11)
b5.new_ab()
b5.hit(2, rbis=2)

# 1. BOS #50 Mookie Betts (X - 12 - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("P4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #66 Bobby Poyner
t6 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #22 Rick Porcello
t6.pitching_substitution(66)

# Defensive change (BOS): #7 Christian Vázquez replaces #12 Brock Holt (PH), playing C, batting 9th
t6.defensive_substitution(9, 7, "2")

# 2. NYM #68 Jeff McNeil (X - X - X)
t6.new_ab()
t6.out("P5")

# 3. NYM #30 Michael Conforto (X - X - X)
t6.new_ab()
t6.pitch_list("b c b s b")
t6.out("G4-3")

# 4. NYM #19 Jay Bruce (X - X - X)
t6.new_ab()
t6.pitch_list("b c f b s")
t6.out("K")


# Bot 6th
# Pitching: NYM #62 Drew Smith
b6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b b b")
b6.out("F7")

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.out("L4")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #66 Bobby Poyner
t7.pitching_substitution(35)

# 5. NYM #21 Todd Frazier (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b c f b")
t7.reach("BB")
t7.advance(2, "9 BB")
t7.advance(3, "16 PB")

# 6. NYM #9  Brandon Nimmo (X - X - 21)
t7.new_ab()
t7.pitch_list("c b 1 c b b b")
t7.reach("BB")
t7.advance(2, "16 PB")

# 7. NYM #22 Dominic Smith (X - 21 - 9)
t7.new_ab()
t7.pitch_list("c t f b f f f f t")
t7.out("KT")

# 8. NYM #26 Kevin Plawecki (X - 21 - 9)
t7.new_ab()
t7.pitch_list("c f b")
t7.out("F8")

# 9. NYM #16 Austin Jackson (X - 21 - 9)
t7.new_ab()
t7.pitch_list("2 b c b")
t7.pb()
t7.out("P3")


# Bot 7th
# Pitching: NYM #47 Drew Gagnon
b7 = game.new_inning()

# Pitching change (NYM): #47 Drew Gagnon replaces #62 Drew Smith
b7.pitching_substitution(47)

# 5. BOS #25 Steve Pearce (X - X - X)
b7.new_ab()
b7.pitch_list("c b c b b")
b7.hit(1)
b7.thrown_out(2, "5 DP6-4-3", 1, 47)

# 6. BOS #5  Ian Kinsler (X - X - 25)
b7.new_ab()
b7.pitch_list("b c b 1 d")
b7.out("DP6-4-3")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.out("P6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #70 Ryan Brasier
t8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #35 Steven Wright
t8.pitching_substitution(70)

# 1. NYM #1  Amed Rosario (X - X - X)
t8.new_ab()
t8.out("F9")

# 2. NYM #68 Jeff McNeil (X - X - X)
t8.new_ab()
t8.pitch_list("c b f f")
t8.out("F8")

# 3. NYM #30 Michael Conforto (X - X - X)
t8.new_ab()
t8.pitch_list("s s s")
t8.out("K")


# Bot 8th
# Pitching: NYM #47 Drew Gagnon
b8 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("f b b")
b8.hit(1)
b8.thrown_out(2, "7 DP5-4-3", 1, 47)

# 9. BOS #7  Christian Vázquez (X - X - 11)
b8.new_ab()
b8.pitch_list("1")
b8.out("DP5-4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f b f f f b")
b8.reach("BB")
b8.advance(2, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b8.new_ab()
b8.hit(1)

# Pitching change (NYM): #35 Jacob Rhame replaces #47 Drew Gagnon
b8.pitching_substitution(35)

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b8.new_ab()
b8.pitch_list("f s b b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #70 Ryan Brasier
t9.pitching_substitution(46)

# 4. NYM #19 Jay Bruce (X - X - X)
t9.new_ab()
t9.pitch_list("b c f b f s")
t9.out("K")

# 5. NYM #21 Todd Frazier (X - X - X)
t9.new_ab()
t9.pitch_list("f b c b f")
t9.out("L8")

# 6. NYM #9  Brandon Nimmo (X - X - X)
t9.new_ab()
t9.pitch_list("b f b")
t9.out("G6-3")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: NYM
# LP: NYM #51 Paul Sewald
game.losing_pitcher(51, is_away_team=True)

# print(game)
game.generate_scorecard()
