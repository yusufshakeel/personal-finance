"""insert default expense subcategories

Revision ID: f7e94b679e9d
Revises: c06ff6834173
Create Date: 2026-03-02 02:31:51.326857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f7e94b679e9d'
down_revision: Union[str, Sequence[str], None] = 'c06ff6834173'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_EXPENSE_SUBCATEGORIES = [
    {
        "id": "7fa434f2-d79b-4948-93c6-eff4fc26a67a",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Food"
    },
    {
        "id": "127b27bc-2e9f-4e5f-8c4a-e0ccc5d436b3",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Snacks"
    },
    {
        "id": "67cce4d5-1b11-40ae-9bf8-a11393d88a2d",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Drinks"
    },
    {
        "id": "8d11ca1a-b59f-456e-bfb4-fd71785203de",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Dining out"
    },
    {
        "id": "90233358-5ea8-430a-b6cd-abb27ddc89a3",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Grocery"
    },
    {
        "id": "e08b66f3-85f3-4a5b-917d-7ff6dab58669",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Food Delivery"
    },
    {
        "id": "06cc34ee-e334-4c5d-90a0-faf469b7b878",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Cafe"
    },
    {
        "id": "36d5f5fe-adb5-4445-a6b9-f65e25138584",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Beverage"
    },
    {
        "id": "97977319-c89c-427b-b4c9-8935b1043222",
        "category_id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Others"
    },
    {
        "id": "7b27ea0e-5b2d-47cd-8995-b6a0a29cd3a7",
        "category_id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Web Hosting"
    },
    {
        "id": "0aab03ea-7909-4cef-8859-68839b28fbbb",
        "category_id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Cloud Service"
    },
    {
        "id": "8d9d4495-9b3e-4f62-a4b9-308eb2ae2d2f",
        "category_id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Web Domain"
    },
    {
        "id": "19f3317e-a613-4518-802d-2b4a2705c7be",
        "category_id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Software Purchase"
    },
    {
        "id": "fcc49b72-ff60-4efc-8db2-b2869b173ac8",
        "category_id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Software License"
    },
    {
        "id": "5e2e1d23-2607-4b67-b6f8-6b674e401682",
        "category_id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Hardware Purchase"
    },
    {
        "id": "e8d6136e-ca03-4270-954e-f87086342382",
        "category_id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Others"
    },
    {
        "id": "afaf1625-9adf-4bca-9dac-d28c3d7579e1",
        "category_id": "dfa5056d-cbe0-4488-80ef-76fcf9c3de3b",
        "name": "Cab and Taxi"
    },
    {
        "id": "0c5ebfaa-de75-4fa6-a7c6-123396d916d0",
        "category_id": "dfa5056d-cbe0-4488-80ef-76fcf9c3de3b",
        "name": "Public Transport"
    },
    {
        "id": "cadb9ad0-53ef-4837-a34b-8d23a4bb203c",
        "category_id": "dfa5056d-cbe0-4488-80ef-76fcf9c3de3b",
        "name": "Train"
    },
    {
        "id": "cec5f50b-cb56-428f-93d2-ffa0e053de19",
        "category_id": "dfa5056d-cbe0-4488-80ef-76fcf9c3de3b",
        "name": "Flight"
    },
    {
        "id": "0306e8eb-615f-4eef-bd67-bab2bcf6af1b",
        "category_id": "dfa5056d-cbe0-4488-80ef-76fcf9c3de3b",
        "name": "Pass",
        "description": "Bus Pass, Cab Pass, Train Pass, etc."
    },
    {
        "id": "18f1c522-755e-42ec-a75b-59e81812ab43",
        "category_id": "dfa5056d-cbe0-4488-80ef-76fcf9c3de3b",
        "name": "Others"
    },
    {
        "id": "7d7acbc9-963a-464f-bd75-61ca21dfe46b",
        "category_id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Internet Bills"
    },
    {
        "id": "c1e1b864-3703-4c48-b280-fdb95dc4f827",
        "category_id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Mobile Bills"
    },
    {
        "id": "7e1e98d1-a3f4-4a17-89c7-75e0b706a0a0",
        "category_id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Maintenance Bills"
    },
    {
        "id": "e312638e-9e43-40d3-b016-13dd60d1df0a",
        "category_id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Electricity Bills"
    },
    {
        "id": "fcf7d0ea-a353-4a93-83b1-f76fdb70aafa",
        "category_id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Water Bills"
    },
    {
        "id": "8c74ace4-ad18-48a2-a0e0-048cb5e295fa",
        "category_id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Warranty and Extended Services"
    },
    {
        "id": "6a4e6cee-476b-4b07-8076-32364eeee9bd",
        "category_id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Others"
    },
    {
        "id": "047a19df-5287-4b85-94a5-f950bf75d4fb",
        "category_id": "8c5cd6e5-96d6-4f37-bf74-c2ecfd0f0914",
        "name": "Streaming Subscription"
    },
    {
        "id": "1d0af583-60c4-4e02-a07e-dbea2e33f7e7",
        "category_id": "8c5cd6e5-96d6-4f37-bf74-c2ecfd0f0914",
        "name": "Newspaper Subscription"
    },
    {
        "id": "c119b190-793e-433b-9681-acc457a20460",
        "category_id": "8c5cd6e5-96d6-4f37-bf74-c2ecfd0f0914",
        "name": "Magazine Subscription"
    },
    {
        "id": "e12891fd-e4ff-41cd-bb51-766709146975",
        "category_id": "8c5cd6e5-96d6-4f37-bf74-c2ecfd0f0914",
        "name": "Subscription Renewals"
    },
    {
        "id": "59ca45e3-2dee-4c7c-86e5-fe0cacf2d263",
        "category_id": "8c5cd6e5-96d6-4f37-bf74-c2ecfd0f0914",
        "name": "Others"
    },
    {
        "id": "f5035801-cd9e-4fc0-928c-3231be8b8932",
        "category_id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "Books"
    },
    {
        "id": "0cfff863-a1e1-4863-9866-dff53fb8d145",
        "category_id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "Tuition Fees"
    },
    {
        "id": "c9c71ccf-a3c2-413e-b3f1-f394c9997693",
        "category_id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "School Fees"
    },
    {
        "id": "2f753c65-6efa-448d-93b3-0a5044eb73be",
        "category_id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "College Fees"
    },
    {
        "id": "1d951753-0942-4786-8082-5455d5e2d8bc",
        "category_id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "Exam Fees"
    },
    {
        "id": "1afb170d-5436-4cce-bd9f-4b9357fb26cf",
        "category_id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "Stationery"
    },
    {
        "id": "92a5239d-9a1a-4a67-a2f6-0e5f97c40e7c",
        "category_id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "Others"
    },
    {
        "id": "c12cf59d-1519-4e15-8167-cf756d842398",
        "category_id": "15bee001-da32-4295-8348-8b9d4097f5c9",
        "name": "Health Insurance"
    },
    {
        "id": "66f796a8-6851-4308-a2b4-71dbdf2f5e26",
        "category_id": "15bee001-da32-4295-8348-8b9d4097f5c9",
        "name": "Life Insurance"
    },
    {
        "id": "617b8394-afb9-4184-b4dd-0a088cbc00db",
        "category_id": "15bee001-da32-4295-8348-8b9d4097f5c9",
        "name": "Vehicle Insurance"
    },
    {
        "id": "39d1028a-a506-4949-a370-ffb7ae5df8c4",
        "category_id": "15bee001-da32-4295-8348-8b9d4097f5c9",
        "name": "Property Insurance"
    },
    {
        "id": "34579a68-eb66-43b0-bbd7-d520fbb9b942",
        "category_id": "15bee001-da32-4295-8348-8b9d4097f5c9",
        "name": "Others"
    },
    {
        "id": "8537e5aa-0071-4210-9319-24d6f5317102",
        "category_id": "15171935-b7b4-4e38-b94f-0962f8225ace",
        "name": "Salon"
    },
    {
        "id": "4170e249-380e-4252-87f0-6c948e2a4a41",
        "category_id": "15171935-b7b4-4e38-b94f-0962f8225ace",
        "name": "Haircut"
    },
    {
        "id": "e3787590-9afd-44ba-ae9d-f94b88dbb17b",
        "category_id": "15171935-b7b4-4e38-b94f-0962f8225ace",
        "name": "Personal Grooming"
    },
    {
        "id": "cf618cae-0a2d-4d5b-847c-caa6a0a32e85",
        "category_id": "15171935-b7b4-4e38-b94f-0962f8225ace",
        "name": "Gym and Fitness"
    },
    {
        "id": "cc6b50b9-e22f-4ab7-954e-53e456fb62f1",
        "category_id": "15171935-b7b4-4e38-b94f-0962f8225ace",
        "name": "Others"
    },
    {
        "id": "9b626231-7052-433d-b74a-0591e6bf9f81",
        "category_id": "f7288b84-4515-4431-b3b1-e6e6b355bddd",
        "name": "Medicine"
    },
    {
        "id": "5b9ab00c-8416-4145-ad02-dabbea3fa4a2",
        "category_id": "f7288b84-4515-4431-b3b1-e6e6b355bddd",
        "name": "Doctor Visit"
    },
    {
        "id": "fbc4246b-f4c5-4e13-8b62-8a3cc7e697e3",
        "category_id": "f7288b84-4515-4431-b3b1-e6e6b355bddd",
        "name": "Hospital"
    },
    {
        "id": "10511651-a46a-47fb-95de-73597c38b911",
        "category_id": "f7288b84-4515-4431-b3b1-e6e6b355bddd",
        "name": "Medfical Tests and Examinations"
    },
    {
        "id": "1edef15f-01cc-4b50-8d46-32420cb17161",
        "category_id": "f7288b84-4515-4431-b3b1-e6e6b355bddd",
        "name": "Others"
    },
    {
        "id": "f619dae5-64d9-473b-bf16-8a6aa5c9f5fa",
        "category_id": "e9ddb85b-dd11-49ba-b6d1-8408271b3489",
        "name": "Loan Repayment"
    },
    {
        "id": "2a5469b0-0431-4734-8d25-cdb0a3810aea",
        "category_id": "e9ddb85b-dd11-49ba-b6d1-8408271b3489",
        "name": "Credit Card Payments"
    },
    {
        "id": "db11e596-6e4c-42b9-bcd9-5f64d116b6dc",
        "category_id": "e9ddb85b-dd11-49ba-b6d1-8408271b3489",
        "name": "Education Loan Payments"
    },
    {
        "id": "6d9ef2de-60a4-44df-8a8a-513a74f65523",
        "category_id": "e9ddb85b-dd11-49ba-b6d1-8408271b3489",
        "name": "Personal Loan Payments"
    },
    {
        "id": "791ca0f9-7525-41db-8c33-10e66f4d3eba",
        "category_id": "e9ddb85b-dd11-49ba-b6d1-8408271b3489",
        "name": "Home Loan Payments"
    },
    {
        "id": "5bf3774d-a8ac-4441-9821-3880ff58210e",
        "category_id": "e9ddb85b-dd11-49ba-b6d1-8408271b3489",
        "name": "Others"
    },
    {
        "id": "7d2d4d35-d9d6-453e-bbc3-8ec1d610c695",
        "category_id": "eb4e687d-b121-4b0d-b4e5-f63fa2277452",
        "name": "Income Tax"
    },
    {
        "id": "42535765-e749-47c5-80ea-29e54ba19b36",
        "category_id": "eb4e687d-b121-4b0d-b4e5-f63fa2277452",
        "name": "Property Tax"
    },
    {
        "id": "de61db9d-eafd-485b-b123-7eb3d6cee9b5",
        "category_id": "eb4e687d-b121-4b0d-b4e5-f63fa2277452",
        "name": "Business Tax"
    },
    {
        "id": "11c125c3-4308-46e5-9aa0-205d4fbf572d",
        "category_id": "eb4e687d-b121-4b0d-b4e5-f63fa2277452",
        "name": "Road Tax"
    },
    {
        "id": "a98346e5-584a-4054-bbf2-631a8ceaae0c",
        "category_id": "eb4e687d-b121-4b0d-b4e5-f63fa2277452",
        "name": "Vehicle Tax"
    },
    {
        "id": "7d9cfbe5-99cc-4729-bb54-deda71daa411",
        "category_id": "eb4e687d-b121-4b0d-b4e5-f63fa2277452",
        "name": "Others"
    },
    {
        "id": "5dc4ccc0-ef2c-488f-834b-acfcc7c5a071",
        "category_id": "cf995521-e754-467a-9204-047dea97c339",
        "name": "Festivals and Celebrations"
    },
    {
        "id": "caa43c85-7857-4123-986f-dfa512ba1dc0",
        "category_id": "cf995521-e754-467a-9204-047dea97c339",
        "name": "Others"
    },
    {
        "id": "51606179-9cc5-4001-945a-dff66bd3ee25",
        "category_id": "9fc2f19c-33d4-4d58-ac77-97106cb67f20",
        "name": "Charity"
    },
    {
        "id": "341c9f75-29f8-4176-8348-4acf82695ca5",
        "category_id": "9fc2f19c-33d4-4d58-ac77-97106cb67f20",
        "name": "Donation"
    },
    {
        "id": "23d6c1b1-960c-47bd-a471-dee4ec192c5d",
        "category_id": "9fc2f19c-33d4-4d58-ac77-97106cb67f20",
        "name": "Others"
    },
    {
        "id": "8730ed2f-68ca-459b-a6e3-2aa632248add",
        "category_id": "62d564fd-e826-4337-91d5-3bd3c56cc6f8",
        "name": "Babysitting & Care Services",
        "description": "Babysitting, Nanny, Daycare, etc."
    },
    {
        "id": "72ab16bf-52a2-4c37-ac22-9129d1e0b771",
        "category_id": "62d564fd-e826-4337-91d5-3bd3c56cc6f8",
        "name": "Baby Essentials",
        "description": "Diapers, Baby Wipes, Baby food, Feeding bottles and accessories, etc."
    },
    {
        "id": "0960dac8-cfe7-4427-b861-68a5d989bfa7",
        "category_id": "62d564fd-e826-4337-91d5-3bd3c56cc6f8",
        "name": "Baby Equipment",
        "description": "Strollers, Cribs, Car Seat, High chairs, etc."
    },
    {
        "id": "eaf03158-d2ae-4db4-bdce-5847d5e0dbbf",
        "category_id": "62d564fd-e826-4337-91d5-3bd3c56cc6f8",
        "name": "Toys & Development Items",
        "description": "Playgroups, Toys, Indoor play areas, Books, etc."
    },
    {
        "id": "3532157e-0fae-4aa8-94a1-51e3804a3bc3",
        "category_id": "62d564fd-e826-4337-91d5-3bd3c56cc6f8",
        "name": "Baby Care Products",
        "description": "Baby powder, Lotion, etc."
    },
    {
        "id": "eccd6703-ccdc-4fa9-b53d-03ab7756aedc",
        "category_id": "62d564fd-e826-4337-91d5-3bd3c56cc6f8",
        "name": "Others"
    },
    {
        "id": "dd50fe3a-e071-4a33-8490-59ae1966a111",
        "category_id": "bb353f9b-e941-4fdf-81a5-3fb80fae748b",
        "name": "Fines and Penalties"
    },
    {
        "id": "35cb3079-6bcc-4773-9b65-5aad602cae4b",
        "category_id": "bb353f9b-e941-4fdf-81a5-3fb80fae748b",
        "name": "Others"
    },
    {
        "id": "12f43cf6-913a-4150-ae72-8f40bc32834c",
        "category_id": "778e12ac-09c6-46eb-949e-6cec4a26e58e",
        "name": "Petrol"
    },
    {
        "id": "36056bb3-90a0-4ac7-bb6c-7f57a80813a4",
        "category_id": "778e12ac-09c6-46eb-949e-6cec4a26e58e",
        "name": "Diesel"
    },
    {
        "id": "c80e952c-3348-4b8c-b9da-63abe7944438",
        "category_id": "778e12ac-09c6-46eb-949e-6cec4a26e58e",
        "name": "CNG"
    },
    {
        "id": "e9caa30f-e964-4c45-afcf-f348370fcc61",
        "category_id": "778e12ac-09c6-46eb-949e-6cec4a26e58e",
        "name": "LPG"
    },
    {
        "id": "caf4572f-1769-4bed-a2e1-70e45f653151",
        "category_id": "778e12ac-09c6-46eb-949e-6cec4a26e58e",
        "name": "EV Charging"
    },
    {
        "id": "5dc9adaf-cc37-4f09-966a-61e0f2312fec",
        "category_id": "778e12ac-09c6-46eb-949e-6cec4a26e58e",
        "name": "Others"
    },
    {
        "id": "76699520-eb7d-4141-afc9-b0fdc89380e3",
        "category_id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Legal Consultation",
        "description": "Lawyer Consultation, Legal Advice, Legal Documentation Review, etc."
    },
    {
        "id": "b7e810e4-8417-4fbe-80f9-e08e46ea3fc9",
        "category_id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Documentation & Agreements",
        "description": "Contract Drafting, Agreement Preparation, Notary Services, Affidavits & Legal Documents, etc."
    },
    {
        "id": "fd9309f0-2496-476c-9b84-5254f159145e",
        "category_id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Court & Dispute Expenses",
        "description": "Court Fees, Case Filing Charges, Legal Representation, etc."
    },
    {
        "id": "ab4ed10c-7acf-44b1-9ff2-b0965fe15af5",
        "category_id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Government Legal Services",
        "description": "Government Legal Documentation, Name Change / Gazette, Legal Certificates, etc."
    },
    {
        "id": "b358fa9b-85e6-4827-a0b5-b2c9f78ded07",
        "category_id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Compliance & Verification",
        "description": "Background Verification, Legal Compliance Fees, etc."
    },
    {
        "id": "bc66a840-e504-47de-bff5-f1ee3f8d4617",
        "category_id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Property Legal",
        "description": "Property Registration, Property Legal Verification, Stamp Duty & Documentation, etc."
    },
    {
        "id": "86021928-11c3-410a-bbf3-fa6b8b659cfd",
        "category_id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Others"
    },
    {
        "id": "87bcb022-6d57-435b-8ae0-302cddee5b03",
        "category_id": "220b7618-85cb-467a-b523-26e1de948668",
        "name": "Parking",
        "description": "Street Parking, Parking Lot / Garage, Mall Parking, Airport Parking, etc."
    },
    {
        "id": "d641049d-5195-4570-80f1-3ca063cdb568",
        "category_id": "220b7618-85cb-467a-b523-26e1de948668",
        "name": "Tolls",
        "description": "Highway Tolls, Bridge Tolls, Tunnel Tolls, Expressway Tolls, etc."
    },
    {
        "id": "346e5a95-333c-4a3e-a26b-8f447ecc0448",
        "category_id": "220b7618-85cb-467a-b523-26e1de948668",
        "name": "Vehicle Access Fees",
        "description": "Congestion Charges (city entry fees in some cities), Fastag / Toll Pass Recharge, etc."
    },
    {
        "id": "65953809-e5d9-42b9-9a76-4c63dac46933",
        "category_id": "220b7618-85cb-467a-b523-26e1de948668",
        "name": "Others"
    },
    {
        "id": "dfa4d14a-ef94-4e94-a638-c00a37a134b6",
        "category_id": "4dbb45cc-45d5-4595-9e1a-696602cfefb2",
        "name": "Food & Daily Needs"
    },
    {
        "id": "497d9670-a7b9-462e-862f-0c8a3c3fb374",
        "category_id": "4dbb45cc-45d5-4595-9e1a-696602cfefb2",
        "name": "Health & Veterinary",
        "description": "Vet Visits, Vaccinations, Medicines, Emergency Care, etc."
    },
    {
        "id": "96234fa8-2307-403d-b3eb-ca518282b1e2",
        "category_id": "4dbb45cc-45d5-4595-9e1a-696602cfefb2",
        "name": "Grooming & Hygiene",
        "description": "Grooming, Pet Shampoo & Hygiene Products, etc."
    },
    {
        "id": "6e6a6e7c-39c3-4802-bc15-d600c7c200b8",
        "category_id": "4dbb45cc-45d5-4595-9e1a-696602cfefb2",
        "name": "Supplies & Accessories",
        "description": "Toys, Collars & Leashes, Bowls & Feeders, Pet Beds, etc."
    },
    {
        "id": "9ed77e5c-8187-471b-a5ff-f61a852b68e3",
        "category_id": "4dbb45cc-45d5-4595-9e1a-696602cfefb2",
        "name": "Services",
        "description": "Pet Boarding, Pet Sitting / Walking, Training Classes, etc."
    },
    {
        "id": "e42bc00d-84d6-41a4-86bf-ce733216bbf3",
        "category_id": "4dbb45cc-45d5-4595-9e1a-696602cfefb2",
        "name": "Others"
    },
    {
        "id": "d7ef709e-7c7f-4a22-b72e-d4fc36cee812",
        "category_id": "b3bd5b9e-2f0c-4303-9e61-625254b010da",
        "name": "Moving Services"
    },
    {
        "id": "49ae0193-7a73-4859-b105-9aa63974ac3c",
        "category_id": "b3bd5b9e-2f0c-4303-9e61-625254b010da",
        "name": "Packing Supplies"
    },
    {
        "id": "ea48c32a-4b6c-4933-9d23-26a5873d11d3",
        "category_id": "b3bd5b9e-2f0c-4303-9e61-625254b010da",
        "name": "Setup Costs"
    },
    {
        "id": "0bc8b568-9fa5-4263-a602-69ead3280fdb",
        "category_id": "b3bd5b9e-2f0c-4303-9e61-625254b010da",
        "name": "Administrative & Documentation"
    },
    {
        "id": "cea47743-736a-474e-b707-a55afd4c9244",
        "category_id": "b3bd5b9e-2f0c-4303-9e61-625254b010da",
        "name": "Move-in Cleaning"
    },
    {
        "id": "3baccd30-a32f-4cad-9e1d-0cad930d4a89",
        "category_id": "b3bd5b9e-2f0c-4303-9e61-625254b010da",
        "name": "Others"
    },
    {
        "id": "13b216b7-7839-4f8b-89db-4105fff1807b",
        "category_id": "09c76317-d954-4a08-91d5-2335fbc8c437",
        "name": "Housing Rent"
    },
    {
        "id": "07181bec-fc66-4335-91ea-4b40f0a1db79",
        "category_id": "09c76317-d954-4a08-91d5-2335fbc8c437",
        "name": "Property Rent",
        "description": "Office Rent, Shop / Workspace Rent, Warehouse / Storage Rent, etc."
    },
    {
        "id": "bdefccd8-7f9a-41e5-b1dc-bd7c5dbcf301",
        "category_id": "09c76317-d954-4a08-91d5-2335fbc8c437",
        "name": "Equipment Rental"
    },
    {
        "id": "1a9e72c4-d365-4c8e-b641-7fb141303fe2",
        "category_id": "09c76317-d954-4a08-91d5-2335fbc8c437",
        "name": "Furniture Rental"
    },
    {
        "id": "47fccad1-0b9e-477f-a599-6aaac1357a0c",
        "category_id": "09c76317-d954-4a08-91d5-2335fbc8c437",
        "name": "Parking Space Rent"
    },
    {
        "id": "8fd8b765-51cf-47e6-8386-c2093deab98b",
        "category_id": "09c76317-d954-4a08-91d5-2335fbc8c437",
        "name": "Others"
    },
    {
        "id": "f0980349-aaec-4418-bfe5-cdbfe6ac4858",
        "category_id": "5ceaa943-7344-4305-91e2-e1f2f63eca5b",
        "name": "Miscellaneous"
    },
    {
        "id": "5b52502b-8cd2-4d4c-9426-4f3f0b731947",
        "category_id": "bfe70105-1935-4535-b841-01bdb68f0ca4",
        "name": "Travel Transport"
    },
    {
        "id": "8e907bcd-2de7-4db2-b9f0-d1096a1b4ad3",
        "category_id": "bfe70105-1935-4535-b841-01bdb68f0ca4",
        "name": "Accommodation"
    },
    {
        "id": "3b2c0224-d0d1-4865-a157-1c6687428c48",
        "category_id": "bfe70105-1935-4535-b841-01bdb68f0ca4",
        "name": "Activities & Experiences"
    },
    {
        "id": "1708f955-a42a-453b-bf16-9c648eb16608",
        "category_id": "bfe70105-1935-4535-b841-01bdb68f0ca4",
        "name": "Others"
    },
    {
        "id": "89000638-e3a7-40bd-97b6-ee0a5e042fd1",
        "category_id": "5c78439d-a7b0-4621-afda-3fa19a749d41",
        "name": "Home Repairs"
    },
    {
        "id": "a216ed53-424b-4fd2-89fe-1220302ae46b",
        "category_id": "5c78439d-a7b0-4621-afda-3fa19a749d41",
        "name": "Electronics Repairs"
    },
    {
        "id": "c0c5dbe8-1ce5-4abd-bfb8-42d9b2fc5b58",
        "category_id": "5c78439d-a7b0-4621-afda-3fa19a749d41",
        "name": "Appliance Repairs"
    },
    {
        "id": "800dc14e-09ee-4f0f-b453-200885b7c656",
        "category_id": "5c78439d-a7b0-4621-afda-3fa19a749d41",
        "name": "Furniture Repairs"
    },
    {
        "id": "964df252-e82f-40e1-8723-42bb557f5fa6",
        "category_id": "5c78439d-a7b0-4621-afda-3fa19a749d41",
        "name": "Others"
    },
    {
        "id": "3ef0512f-dee6-4e35-82c4-42a6519c90c1",
        "category_id": "fd7d8bf9-4712-4e32-b423-dbd306047ccc",
        "name": "Laundry Service"
    },
    {
        "id": "43a265f7-46dd-494e-a74c-ab8440ec059b",
        "category_id": "fd7d8bf9-4712-4e32-b423-dbd306047ccc",
        "name": "Dry Cleaning"
    },
    {
        "id": "e97d874c-b71c-49cf-a821-bec8b86ccbf5",
        "category_id": "fd7d8bf9-4712-4e32-b423-dbd306047ccc",
        "name": "Ironing & Pressing"
    },
    {
        "id": "e8ec37b5-403e-469e-a5da-8c34774de3fb",
        "category_id": "fd7d8bf9-4712-4e32-b423-dbd306047ccc",
        "name": "Laundry Supplies"
    },
    {
        "id": "6b239e68-b004-4d44-b10e-3e12c76e65b2",
        "category_id": "fd7d8bf9-4712-4e32-b423-dbd306047ccc",
        "name": "Others"
    },
    {
        "id": "e9231246-2c42-4784-8e69-ef2855e7c2b9",
        "category_id": "ed73c774-54d5-46a5-88df-a49eea5d99e9",
        "name": "Cleaning & Regular Servicing"
    },
    {
        "id": "dbe3ac3e-b0af-4df2-a93f-fd2da08ac513",
        "category_id": "ed73c774-54d5-46a5-88df-a49eea5d99e9",
        "name": "Parts Replacement, Accessories & Upgrades"
    },
    {
        "id": "060af3f8-1634-42ab-b102-d1ea057f7c0f",
        "category_id": "ed73c774-54d5-46a5-88df-a49eea5d99e9",
        "name": "Mechanical Repairs"
    },
    {
        "id": "0d5c904a-d3ec-426a-bbef-9cb04e7259d3",
        "category_id": "ed73c774-54d5-46a5-88df-a49eea5d99e9",
        "name": "Others"
    }
]


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    expense_subcategories = sa.table(
        "expense_subcategories",
        sa.column("id", sa.UUID),
        sa.column("category_id", sa.String),
        sa.column("name", sa.String),
        sa.column("description", sa.String),
    )

    # Normalize data: Ensure every dict has a 'description' key (defaulting to None)
    normalized_data = [
        {
            "id": kv["id"],
            "category_id": kv["category_id"],
            "name": kv["name"],
            "description": kv.get("description")  # Returns None if key is missing
        }
        for kv in DEFAULT_EXPENSE_SUBCATEGORIES
    ]

    connection.execute(expense_subcategories.insert(), normalized_data)


def downgrade() -> None:
    """Downgrade schema."""
    connection = op.get_bind()

    subcategory_ids = [subcategory["id"] for subcategory in DEFAULT_EXPENSE_SUBCATEGORIES]

    connection.execute(
        sa.text(
            """
            DELETE FROM expense_subcategories
            WHERE id IN :ids
            """
        ).bindparams(ids=tuple(subcategory_ids))  # Convert to tuple for the IN clause
    )
