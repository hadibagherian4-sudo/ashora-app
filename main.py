import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';

import '../data/fake_db.dart';
import '../models/comment.dart';
import '../models/referee_profile.dart';
import '../models/submission.dart';
import '../widgets/app_header.dart';
import '../widgets/primary_button.dart';

class NexaSystemNavigator extends StatefulWidget {
  const NexaSystemNavigator({super.key});

  @override
  State<NexaSystemNavigator> createState() => _NexaSystemNavigatorState();
}

class _NexaSystemNavigatorState extends State<NexaSystemNavigator> {
  String currentStep = "welcome";
  String userRole = "guest"; // user, manager, referee
  String loginPhone = "";
  String loginId = "";
  int navIdx = 0;

  final fieldCommittees = const [
    "۱. حوزه معماری و منظر",
    "۲. حوزه فنی و مهندسی",
    "۳. حوزه برنامه‌ریزی و مدیریت پروژه",
    "۴. حوزه کنترل پروژه",
    "۵. حوزه نقشه‌برداری و فتوگرامتری",
    "۶. حوزه بتن",
    "۷. حوزه هوش مصنوعی",
    "۸. حوزه ICT",
    "۹. حوزه نگهداری و ماشین‌آلات (نت)",
    "۱۰. حوزه کنترل کیفیت (QC)",
    "۱۱. حوزه HSSE",
    "۱۲. حوزه BIM",
    "۱۳. حوزه آسفالت",
    "۱۴. حوزه مالی و حسابداری",
  ];

  final universityMajors = const [
    "عمران",
    "معماری",
    "مکانیک",
    "برق",
    "هوش مصنوعی",
    "صنایع",
    "مدیریت",
    "حقوق",
  ];

  final pName = TextEditingController();
  final pId = TextEditingController();
  final pMob = TextEditingController();

  void resetApp() => setState(() {
        currentStep = "welcome";
        userRole = "guest";
        navIdx = 0;
        loginPhone = "";
        loginId = "";
      });

  @override
  void dispose() {
    pName.dispose();
    pId.dispose();
    pMob.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    switch (currentStep) {
      case "welcome":
        return buildWelcome();
      case "login":
        return buildLogin();
      case "verify":
        return buildVerify();
      default:
        return buildDashboard();
    }
  }

  Widget buildWelcome() => Scaffold(
        body: Column(
          children: [
            const AppHeader(subtitle: "ورود به سامانه پایش تخصصی محتوا"),
            Padding(
              padding: const EdgeInsets.all(25),
              child: Column(
                children: [
                  const Text(
                    "لطفاً نوع کاربری خود را تعیین کنید:",
                    style: TextStyle(
                        fontWeight: FontWeight.bold, color: Colors.black),
                  ),
                  const SizedBox(height: 25),
                  roleBtn("کاربر عادی (پرسنل اجرایی)", "user"),
                  roleBtn("داور تخصصی / نخبگان دانشی", "referee"),
                  roleBtn("مدیر سامانه", "manager"),
                ],
              ),
            ),
          ],
        ),
      );

  Widget roleBtn(String title, String role) => Padding(
        padding: const EdgeInsets.only(bottom: 12),
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.white,
            foregroundColor: Colors.black,
            side: const BorderSide(color: Color(0xFF002d5b), width: 2),
            minimumSize: const Size(double.infinity, 55),
          ),
          onPressed: () => setState(() {
            userRole = role;
            currentStep = "login";
          }),
          child: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        ),
      );

  Widget buildLogin() => Scaffold(
        body: Padding(
          padding: const EdgeInsets.all(30),
          child: Column(
            children: [
              const SizedBox(height: 80),
              lbl("شماره همراه فعال سامانه :"),
              TextField(
                onChanged: (v) => loginPhone = v,
                decoration: const InputDecoration(border: OutlineInputBorder()),
              ),
              const SizedBox(height: 15),
              lbl("کد ملی کاربر (رمز ورود) :"),
              TextField(
                onChanged: (v) => loginId = v,
                obscureText: true,
                decoration: const InputDecoration(border: OutlineInputBorder()),
              ),
              const SizedBox(height: 25),
              PrimaryButton(
                title: "درخواست کد تایید هویت",
                onPressed: () => setState(() => currentStep = "verify"),
              ),
            ],
          ),
        ),
      );

  Widget buildVerify() => Scaffold(
        body: Center(
          child: PrimaryButton(
            title: "تایید و ورود نهایی",
            width: 250,
            onPressed: handleFinalLogin,
          ),
        ),
      );

  void handleFinalLogin() {
    if (userRole == "referee") {
      final ok = FakeDb.referees.any(
          (r) => r.phone == loginPhone.trim() && r.nationalId == loginId.trim());
      if (!ok) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text("هویت داوری شما توسط مدیر ثبت نشده است")),
        );
        return;
      }
    }
    setState(() => currentStep = "main");
  }

  Widget buildDashboard() {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "نکسا | میز $userRole",
          style: const TextStyle(
            color: Color(0xFF002d5b),
            fontWeight: FontWeight.bold,
            fontSize: 14,
          ),
        ),
        actions: [
          IconButton(
            onPressed: resetApp,
            icon: const Icon(Icons.logout, color: Colors.red),
          )
        ],
      ),
      body: buildPage(),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: navIdx,
        selectedItemColor: const Color(0xFF002d5b),
        onTap: (i) => setState(() => navIdx = i),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "میز کار"),
          BottomNavigationBarItem(
              icon: Icon(Icons.forum_outlined), label: "تالار گفتگو"),
          BottomNavigationBarItem(
              icon: Icon(Icons.person_pin), label: "پروفایل"),
        ],
      ),
    );
  }

  Widget buildPage() {
    if (navIdx == 1) return buildChatForum();
    if (navIdx == 2) return buildProfileEditor();

    switch (userRole) {
      case "user":
        return buildUserWorkbench();
      case "manager":
        return buildManagerWorkbench();
      case "referee":
        return buildRefereeWorkbench();
      default:
        return const Center(child: Text("نقش کاربری نامشخص است"));
    }
  }

  // ---------------- USER ----------------
  Widget buildUserWorkbench() => DefaultTabController(
        length: 4,
        child: Column(
          children: [
            const TabBar(
              isScrollable: true,
              labelColor: Color(0xFF002d5b),
              indicatorColor: Color(0xFFfbbf24),
              tabs: [
                Tab(text: "ویترین دانش"),
                Tab(text: "ارسال محتوا"),
                Tab(text: "وضعیت پیگیری"),
                Tab(text: "پیشنهاد موضوعات"),
              ],
            ),
            Expanded(
              child: TabBarView(
                children: [
                  buildShowcase(),
                  buildSubmitForm(),
                  buildTracking(),
                  buildUniversityList(),
                ],
              ),
            )
          ],
        ),
      );

  Widget buildShowcase() => ListView.builder(
        itemCount: FakeDb.submissions.length,
        itemBuilder: (c, i) => buildContentCard(FakeDb.submissions[i]),
      );

  Widget buildContentCard(Submission s) => Card(
        margin: const EdgeInsets.all(15),
        clipBehavior: Clip.antiAlias,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15),
          side: BorderSide(color: Colors.grey.shade200),
        ),
        child: Column(
          children: [
            Image.asset(
              s.imgPath,
              height: 180,
              width: double.infinity,
              fit: BoxFit.cover,
              errorBuilder: (c, e, st) => Container(
                height: 180,
                color: Colors.blue.shade50,
                child: const Icon(Icons.engineering),
              ),
            ),
            ListTile(
              title: Text(s.title,
                  style: const TextStyle(
                      fontWeight: FontWeight.bold, color: Colors.black)),
              subtitle: Text("${s.field} | کد دانشی: ${s.knowledgeCode}"),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10),
              child: Row(
                children: [
                  IconButton(
                    icon:
                        const Icon(Icons.favorite_border, color: Colors.red),
                    onPressed: () => setState(() => s.likes++),
                  ),
                  Text(" پسندیدن (${s.likes})",
                      style: const TextStyle(
                          fontWeight: FontWeight.bold, fontSize: 11)),
                  const Spacer(),
                  TextButton(
                    onPressed: () => openComments(s),
                    child: const Text("نظرات",
                        style: TextStyle(fontWeight: FontWeight.bold)),
                  )
                ],
              ),
            )
          ],
        ),
      );

  void openComments(Submission s) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      builder: (c) => Padding(
        padding: EdgeInsets.only(
          bottom: MediaQuery.of(c).viewInsets.bottom,
          top: 15,
          left: 15,
          right: 15,
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text("بخش تبادل دیدگاه‌های تخصصی",
                style: TextStyle(fontWeight: FontWeight.bold)),
            SizedBox(
              height: 200,
              child: ListView.builder(
                itemCount: s.comments.length,
                itemBuilder: (cc, ii) => ListTile(
                  title: Text(
                    s.comments[ii].user,
                    style: const TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: Colors.blueGrey,
                    ),
                  ),
                  subtitle: Text(s.comments[ii].text,
                      style: const TextStyle(color: Colors.black)),
                  trailing: userRole == "manager"
                      ? IconButton(
                          icon: const Icon(Icons.delete, color: Colors.red),
                          onPressed: () {
                            setState(() => s.comments.removeAt(ii));
                            Navigator.pop(c);
                          },
                        )
                      : null,
                ),
              ),
            ),
            TextField(
              decoration: const InputDecoration(
                hintText: "درج دیدگاه نخبگان...",
                border: OutlineInputBorder(),
              ),
              onSubmitted: (v) {
                setState(() {
                  s.comments.add(Comment(id: "x", user: "همکار پروژه", text: v));
                });
                Navigator.pop(c);
              },
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  Widget buildSubmitForm() => SingleChildScrollView(
        padding: const EdgeInsets.all(25),
        child: Column(
          children: [
            const TextField(
              decoration:
                  InputDecoration(labelText: "عنوان سناریو / محتوای فنی"),
            ),
            const SizedBox(height: 10),
            DropdownButtonFormField<String>(
              decoration: const InputDecoration(labelText: "حوزه تخصصی پیشنهادی"),
              items: fieldCommittees
                  .map((e) => DropdownMenuItem(value: e, child: Text(e)))
                  .toList(),
              onChanged: (_) {},
            ),
            const SizedBox(height: 15),
            filePickerField(),
            const SizedBox(height: 30),
            PrimaryButton(
              title: "ثبت نهایی و ارسال به سازمان",
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text("با موفقیت ثبت گردید")),
                );
              },
            ),
          ],
        ),
      );

  Widget filePickerField() => InkWell(
        onTap: () async {
          final res = await FilePicker.platform.pickFiles();
          if (res != null && mounted) {
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(content: Text("فایل با موفقیت بارگذاری شد.")),
            );
          }
        },
        child: Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            border: Border.all(color: Colors.grey),
            borderRadius: BorderRadius.circular(10),
            color: Colors.grey.shade50,
          ),
          child: const Row(
            children: [
              Icon(Icons.attachment),
              SizedBox(width: 15),
              Text("پیوست فایل (حافظه گوشی یا رایانه)"),
            ],
          ),
        ),
      );

  Widget buildTracking() => ListView.builder(
        itemCount: 1,
        itemBuilder: (c, i) => const ListTile(
          title: Text("طرح: بهسازی لایه ها"),
          subtitle: Text("وضعیت: در حال ارزیابی کمیته تخصصی"),
          trailing: Icon(Icons.timer),
        ),
      );

  Widget buildUniversityList() => ListView.builder(
        itemCount: universityMajors.length,
        itemBuilder: (c, i) => Card(
          child: ListTile(
            title: Text("رشته ${universityMajors[i]}"),
            subtitle: const Text("پیشنهاد موضوعات خدمت و پایان‌نامه"),
          ),
        ),
      );

  // ---------------- MANAGER ----------------
  Widget buildManagerWorkbench() => DefaultTabController(
        length: 2,
        child: Column(
          children: [
            const TabBar(
              labelColor: Color(0xFF002d5b),
              tabs: [
                Tab(text: "میز ارجاع ارشد"),
                Tab(text: "ثبت داور تخصصی"),
              ],
            ),
            Expanded(
              child: TabBarView(
                children: [
                  ListView.builder(
                    itemCount: 2,
                    itemBuilder: (c, i) => ListTile(
                      title: const Text("سناریو فنی تثبیت روسازی"),
                      subtitle: const Text("فرستنده: کارگاه ساوه | منتظر ارجاع"),
                      trailing: ElevatedButton(
                        onPressed: showReferralDialog,
                        child: const Text("بررسی و ارجاع"),
                      ),
                    ),
                  ),
                  addRefereeForm(),
                ],
              ),
            )
          ],
        ),
      );

  void showReferralDialog() {
    showDialog(
      context: context,
      builder: (c) => AlertDialog(
        title: const Text("ارجاع به کمیته و داور:"),
        content: DropdownButton<RefereeProfile>(
          isExpanded: true,
          items: FakeDb.referees
              .map(
                (r) => DropdownMenuItem(
                  value: r,
                  child: Text("${r.firstName} ${r.lastName} - ${r.field}"),
                ),
              )
              .toList(),
          onChanged: (v) {
            Navigator.pop(c);
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(content: Text("به نخبگان حوزه مربوطه ارجاع شد.")),
            );
          },
        ),
      ),
    );
  }

  Widget addRefereeForm() => SingleChildScrollView(
        padding: const EdgeInsets.all(25),
        child: Column(
          children: [
            const Text("تعریف داور فنی (صدور اجازه ورود)"),
            const TextField(decoration: InputDecoration(labelText: "نام نخبگان")),
            const TextField(decoration: InputDecoration(labelText: "شماره همراه")),
            const TextField(
                decoration: InputDecoration(labelText: "کد ملی (ID ورود)")),
            const SizedBox(height: 20),
            PrimaryButton(
              title: "تایید و ساخت پنل نخبگان",
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text("داور جدید با موفقیت ثبت شد")),
                );
              },
            )
          ],
        ),
      );

  // ---------------- REFEREE (placeholder) ----------------
  Widget buildRefereeWorkbench() => const Center(
        child: Text(
          "پنل داور (در نسخه گیت‌هابی تفکیک‌شده)\n"
          "— این بخش را در قدم بعدی دقیقاً مثل منطق شما کامل می‌کنم —",
          textAlign: TextAlign.center,
        ),
      );

  // ---------------- COMMON ----------------
  Widget buildChatForum() => Column(
        children: [
          const Expanded(
            child: Center(
              child: Text(
                "🗨️ تالار گفتگو سراسری نکسا\n"
                "(کاربران گرامی، چت عمومی غیرفعال است. روی نام داور کلیک کنید.)",
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.black),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(15),
            child: TextField(
              decoration: const InputDecoration(
                hintText: "درج پیام خصوصی در گفتگو با نخبگان...",
                suffixIcon: Icon(Icons.send, color: Colors.blue),
                border: OutlineInputBorder(),
              ),
            ),
          ),
          const SizedBox(height: 50),
        ],
      );

  Widget buildProfileEditor() => SingleChildScrollView(
        padding: const EdgeInsets.all(25),
        child: Column(
          children: [
            const CircleAvatar(
              radius: 50,
              backgroundColor: Color(0xFF002d5b),
              child: Icon(Icons.person, color: Colors.white, size: 50),
            ),
            const SizedBox(height: 25),
            TextField(
              controller: pName,
              decoration: const InputDecoration(
                labelText: "نام و نام خانوادگی",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: pId,
              decoration: const InputDecoration(
                labelText: "کد ملی شخصی",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: pMob,
              decoration: const InputDecoration(
                labelText: "شماره همراه سازمانی",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 30),
            PrimaryButton(title: "ذخیره نهایی اطلاعات", onPressed: () {}),
          ],
        ),
      );

  Widget lbl(String t) => Align(
        alignment: Alignment.centerRight,
        child: Text(
          t,
          style: const TextStyle(
            color: Colors.black,
            fontWeight: FontWeight.bold,
            fontSize: 13,
          ),
        ),
      );
}
