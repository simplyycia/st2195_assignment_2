{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee793f4d-a94d-4a80-ae4c-0822b9a0a6b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "27dadc51-ca21-4718-9357-d9c2cfe76b4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# The User-Agent is a string that a a web browser (or app) \n",
    "# sends in HTTP headers when making a request to a server. \n",
    "# Wikipedia sometimes blocks requests with generic hehaders\n",
    "# Typically, a User-Agent string from a browser includes info \n",
    "# about the software, version, rendering engine, OS, etc.\n",
    "# Google search for \"my user agent\" "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5f0e0ad4-5a60-4216-81b7-ea23e5fa853d",
   "metadata": {},
   "outputs": [],
   "source": [
    "headers = {\n",
    "    \"User-Agent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0 Safari/537.36\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a066ebe8-9302-4e2d-8dc2-cf664b2cc44e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "200\n",
      "{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept': '*/*', 'Connection': 'keep-alive'}\n"
     ]
    }
   ],
   "source": [
    "url = \"https://en.wikipedia.org/wiki/Delimiter-separated_values\"\n",
    "response = requests.get(url, headers=headers)\n",
    "print(response.status_code)      # should print 200 if OK\n",
    "print(response.request.headers)  # verify your header worked"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "27680435-2993-4834-8254-2d55cd1b0c73",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(response.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "67980b36-3dac-4ab8-86b1-f1f94b0f49a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"Date\",\"Pupil\",\"Grade\"\n",
      "\"25 May\",\"Bloggs, Fred\",\"C\"\n",
      "\"25 May\",\"Doe, Jane\",\"B\"\n",
      "\"15 July\",\"Bloggs, Fred\",\"A\"\n",
      "\"15 April\",\"Muniz, Alvin \"\"Hank\"\"\",\"A\"\n",
      "\n"
     ]
    }
   ],
   "source": [
    "ths = soup.find(id='Example')       #use id='Example' to start search at this id\n",
    "table = ths.findNext('pre').text    #does next 'pre' tag contain the text we want\n",
    "print(table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a9a622ba-1b03-4300-bc9e-2296aee2201a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#save data to csv file\n",
    "with open(\"wikipedia_example.csv\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5675b8db-a1d2-40bf-9ad9-30006e3612a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Date                Pupil Grade\n",
      "0    25 May         Bloggs, Fred     C\n",
      "1    25 May            Doe, Jane     B\n",
      "2   15 July         Bloggs, Fred     A\n",
      "3  15 April  Muniz, Alvin \"Hank\"     A\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"wikipedia_example.csv\")\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12dbc26b-390e-4cd4-8a17-5d307131cc52",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
