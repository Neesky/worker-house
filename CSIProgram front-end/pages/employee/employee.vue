<template>
	<view>
		<view v-if="add_able">
			<uni-fab :pattern="pattern" :popMenu=false horizontal="right" @fabClick="fabClick"></uni-fab>
		</view>
		
		<u-modal v-model="showdelete" :content="contentdelete" @confirm="confirmdelete"  :show-confirm-button="true" :show-cancel-button="true"></u-modal>
	
		
		<view>
			<u-toast ref="uToast" />
		</view>
			
		<u-modal v-model="show" @confirm="confirm" @cancel="cancel" title="筛选条件" :show-cancel-button=true>
			<u-form style="margin-left:10px;" :model="form" ref="uForm">
				<u-form-item label="姓名">
					<u-input class="input" v-model="form.name" />
				</u-form-item>
				<u-form-item label="手机">
					<u-input class="input" v-model="form.telephone" />
				</u-form-item>
				<u-form-item label-width=120rpx label="身份证号">
					<u-input class="input1" v-model="form.idnum" />
				</u-form-item>

				<u-form-item label="性别">
					<u-input class="input input2" v-model="form.sex" type="select" border="border"
						@click="showsex = true" />
					<u-action-sheet :list="actionSheetListsex" v-model="showsex" @click="actionSheetCallbacksex">
					</u-action-sheet>
				</u-form-item>
				<u-form-item label="职位">
					<u-input class="input input2" v-model="form.pos" type="select" border="border"
						@click="showpos = true" />
				</u-form-item>
				<u-action-sheet :list="actionSheetListpos" v-model="showpos" @click="actionSheetCallbackpos">
				</u-action-sheet>
				</u-form-item>
				<u-form-item label-width=120rpx label="所属部门">
					<u-input class="input1 input2" v-model="form.branchnum" type="select" border="border"
						@click="showbranch = true" />
					<u-action-sheet :list="actionSheetListbranch" v-model="showbranch"
						@click="actionSheetCallbackbranch"></u-action-sheet>
				</u-form-item>
			</u-form>
		</u-modal>
		
		<view class="content"> 
			<image class="search" src="/static/search.png" @tap="clicksearch"></image>
		</view>
		
		<u-index-list :scrollTop="scrollTop">
			<view v-for="(item, index) in indexList" :key="index" >
				<u-index-anchor :index="item" />
				<u-swipe-action :index="index2" v-for="(item1, index2) in nameList[item]" :key="index2" @click="click" @open="changeright(item1)"
					 :options="item1.status == '0' ? options1 : options2">
					<view class="item u-border-bottom" @click="clickemployee(item1)">
						<image mode="aspectFill" :src="item1.sex == '1' ? imgUrl : imgUrl2" />
						<view class="vertical">
							<view class="line">
								<text :iterchar="item1.name" class="name">{{ item1.name }}</text>
								<text class="fontgap">{{ item1.departmentName }}</text>
							</view>
							<view class="line">
								<text class="title">性别: </text>
								<text class="title">{{item1.sex == '1' ? '男' : '女'  }}</text>
							</view>
							<view class="line">
								<text class="title">职位: </text>
								<text class="title">{{ item1.jobName }}</text>
							</view>
						</view>
					</view>
					<!-- <u-gap height="20" bg-color="#9EC2EC"></u-gap> -->
				</u-swipe-action>
			</view>
		</u-index-list> 
				
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	import pinyin from '../../node_modules/js-pinyin'
	export default {
		data() {
			return {
				add_able:true,
				
				showdelete:false,
				contentdelete:"确认删除此员工？",
				
				iterchar:{},
				scrollTop: 0,
				indexList: [],
				nameList:{},
				
				employeesex:'0',
				show: false,
				showsex: false,
				showpos: false,
				showbranch: false,
				pattern: {
					color: 'gray',
					backgroundColor: '#FFFFFF',
					selectedColor: '#9EC2EC',
					buttonColor: '#9EC2EC'
				},
				actionSheetListsex: [
					{
						text: '男'
					},
					{
						text: '女'
					}
				],
				actionSheetListpos: [
					
				],
				actionSheetListbranch: [
					
				],
				form: {
					name: '',
					telephone: '',
					idnum: '',
					sex: '',
					pos: '',
					branchnum: ''
				},
				imgUrl: "/static/boy.png",
				imgUrl2: "/static/girl.png",
				list: [],
				disabled: false,
				btnWidth: 180,
				show: false,
				options1: [{
						text: '修改',
						style: {
							backgroundColor: '#9EB7EC'
						}
					},
					{
						text: '删除',
						style: {
							backgroundColor: '#dd524d'
						}
					}
				],
				options2: [{
						text: '修改',
						style: {
							backgroundColor: '#9EB7EC'
						}
					}
				]
			};
		},
		onPageScroll(e) {
			this.scrollTop = e.scrollTop;
		},
		onBackPress(){
			uni.reLaunch({
				url:'/pages/home/home'
			})
			return true;
		},
		onLoad() {
			if(uni.getStorageSync('global_status')=="0"){
				this.options1=[];
				this.options2=[];
				this.add_able=false;
			}
		},
		onShow() {
			
			this.actionSheetListbranch = []; //每次刷新页面时清空job和department的列表，不然会发生重复
			this.actionSheetListpos = [];
			this.indexList = [];
			this.nameList = [];
			this.computeNameList(uni.getStorageSync('global_employee_list'));	
			this.department_list = uni.getStorageSync('global_department_list');
			for (let i = 0; i < this.department_list.length; i++) {
				let t = {
					"text": ''
				};
				t.text = this.department_list[i].departmentName;
				this.actionSheetListbranch.push(t);
			}
			
			this.job_list = uni.getStorageSync('global_job_list')
			for (let i = 0; i < this.job_list.length; i++) {
				let t = {
					"text": ''
				};
				t.text = this.job_list[i].jobName;
				this.actionSheetListpos.push(t);
			}	
		},
		methods: {
			//将返回数据的名字按字母排序构建新列表
			computeNameList(namedata){
				let adminListDatas = namedata;
				let obj = {};
				let arr2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
							"V", "W", "X", "Y", "Z"];
				for (let i = 0; i < arr2.length; i++) {
					let temp = [];
					for (let j = 0;j < adminListDatas.length; j++){
						let t = {
							"name": '',
							"sex": '',
							'departmentName':'',
							'jobName':'',
							'id':'',
							
							"departmentRemark": '',
							"jobName": '',
							"jobRemark": '',
							"cardId": '',
							"address": '',
							"postCode": '',
							"tel": '',
							"phone": '',
							"QQNumber": '',
							"email": '',
							"party": '',
							"birthday": '',
							"race": '',
							"education": '',
							"speciality": '',
							"hobby": '',
							"remark": '',
							"createDate": '',
							"status": ''
						};
						let pinyin = require('js-pinyin');
						pinyin.setOptions({checkPolyphone: false, charCase: 0});
						let checkname = pinyin.getFullChars(adminListDatas[j].name);
						if (arr2[i] == checkname[0].toUpperCase()) {
							t.name = adminListDatas[j].name;
							t.sex = adminListDatas[j].sex;
							t.departmentName = adminListDatas[j].departmentName;
							t.jobName = adminListDatas[j].jobName;
							t.id = adminListDatas[j].id;
							
							t.departmentRemark = adminListDatas[j].departmentRemark;
							t.jobName = adminListDatas[j].jobName;
							t.jobRemark = adminListDatas[j].jobRemark;
							t.cardId = adminListDatas[j].cardId;
							t.address = adminListDatas[j].address;
							t.postCode = adminListDatas[j].postCode;
							t.tel = adminListDatas[j].tel;
							t.phone = adminListDatas[j].phone;
							t.QQNumber = adminListDatas[j].QQNumber;
							t.email = adminListDatas[j].email;
							t.party = adminListDatas[j].party;
							t.birthday = adminListDatas[j].birthday;
							t.race = adminListDatas[j].race;
							t.education = adminListDatas[j].education;
							t.speciality = adminListDatas[j].speciality;
							t.hobby = adminListDatas[j].hobby;
							t.remark = adminListDatas[j].remark;
							t.createDate = adminListDatas[j].createDate;
							t.status = adminListDatas[j].status;
							
							temp.push(t);
						}
					}
					if (temp.length != 0){
						obj[arr2[i]] = temp;
						this.indexList.push(arr2[i]);
					}
				}
				this.nameList = obj;
				console.log(this.indexList);
				console.log(this.nameList);
			},
			fabClick() {
				uni.navigateTo({
					url: '../addemployee/addemployee'
				})
			},
			clicksearch() {
				this.show = true;
			},
			confirm() {
				this.indexList = [];
				this.nameList = [];
				console.log(this.form.pos);
				console.log(this.form.branchnum);
				if (this.form.sex == '男'){
					this.employeesex = '1';
				}
				else if (this.form.sex == '女'){
					this.employeesex = '2';
				}
				else{
					this.employeesex = '0';
				}
				
				uni.request({
					url: helper.websiteUrl+'/employee/search',
					method: 'POST',
					data: {
						"departmentName": this.form.branchnum,
						"jobName": this.form.pos,
						"name": this.form.name,
						"cardId": this.form.idnum,
						"phone": this.form.telephone,
						"sex": this.employeesex
					},
					header: {
						"token": uni.getStorageSync('token')
					},
					success: (res) => {
						if (res.data.code == 200){
							console.log('查找员工信息成功');
							this.list = res.data.data;
							console.log(res.data.data);
							this.computeNameList(res.data.data);
							
							this.$refs.uToast.show({
								title: '查找员工成功',
								type: 'success'
							})
						}
						else{
							this.$refs.uToast.show({
								title: '查找员工失败',
								type: 'error'
							})
						}
					}
				});
				
				
				this.form.name = '';
				this.form.telephone = '';
				this.form.idnum = '';
				this.form.branchnum = '';
				this.form.sex = '';
				this.form.pos = '';
				this.form.branchnum = '';
			},
			cancel() {
				this.form.name = '';
				this.form.telephone = '';
				this.form.idnum = '';
				this.form.branchnum = '';
				this.form.sex = '';
				this.form.pos = '';
				this.form.branchnum = '';
			},
			actionSheetCallbacksex(index) {
				this.showsex = true;
				this.form.sex = this.actionSheetListsex[index].text;
			},
			actionSheetCallbackpos(index) {
				this.showpos = true;
				this.form.pos = this.actionSheetListpos[index].text;
			},
			actionSheetCallbackbranch(index) {
				this.showbranch = true;
				this.form.branchnum = this.actionSheetListbranch[index].text;
			},
			
			changeright(item){
				this.iterchar = item;
				console.log(this.iterchar);
			},
			
			click(index,index1) {
				console.log("index1");
				console.log(index1);
				if (index1 == 1) {
					this.showdelete = true;
				} 
				else {
					// this.list[index].show = false;
					uni.setStorageSync('empolyeeId',this.iterchar.id);
					uni.navigateTo({
						url:'../editemployee/editemployee'
					})
				}
			},
			
			confirmdelete(){
				uni.request({
					url: helper.websiteUrl+'/employee/delete',
					data: {
						"id": this.iterchar.id,
						"departmentName": this.iterchar.departmentName,
						"departmentRemark": this.iterchar.departmentRemark,
						"jobName": this.iterchar.jobName,
						"jobRemark": this.iterchar.jobRemark,
						"name":this.iterchar.name,
						"cardId": this.iterchar.idnum,
						"address": this.iterchar.address,
						"postCode": this.iterchar.postCode,
						"tel": this.iterchar.tel,
						"phone": this.iterchar.phone,
						"QQNumber": this.iterchar.branchnum,
						"email": this.iterchar.email,
						"sex": this.iterchar.sex,
						"party": this.iterchar.party,
						"birthday": this.iterchar.birthday,
						"race": this.iterchar.race,
						"education": this.iterchar.education,
						"speciality": this.iterchar.speciality,
						"hobby": this.iterchar.hobby,
						"remark": this.iterchar.remark,
						"createDate": this.iterchar.createDate,
						"status": this.iterchar.status
					},
					method: 'POST',
					header: {
						"token": uni.getStorageSync('token')
					},
					success: (res) => {
						if (res.data.code == 200) {
							this.$refs.uToast.show({
								title: '删除员工成功',
								type: 'success'
							})
							console.log("删除员工成功");
							
							uni.request({
								url: helper.websiteUrl+'/employee/getAll',
								method: 'GET',
								header: {
									"token": uni.getStorageSync('token')
								},
								success: (res) => {
									if (res.data.code == 200){
										uni.setStorageSync('global_employee_list',res.data.data);
									}
									else{
										this.$refs.uToast.show({
											title: '获取员工信息失败',
											type: 'error'
										})
									}
								}
							});
							
							
							// this.list.splice(index, 1);
							
							//后来加上的
							this.indexList = [];
							this.nameList = [];
							uni.request({
								url: helper.websiteUrl+'/employee/getAll',
								method: 'GET',
								heads: {
									'content-type': 'application/x-www-form-urlencoded'
								},
								header: {
									"token": uni.getStorageSync('token')
								},
								success: (res) => {
									if (res.data.code == 200){
										console.log('获取员工信息成功');
										this.list = res.data.data;
										console.log(res.data.data);
										this.computeNameList(res.data.data);	
									}
									else{
										this.$refs.uToast.show({
											title: '获取最新信息失败',
											type: 'error'
										})
									}
								}
							});
							// 后来加上的
						} 
						else {
							this.$refs.uToast.show({
								title: '删除员工失败',
								type: 'error'
							})
						}
					}
				})
			},
			
			// 如果打开一个的时候，不需要关闭其他，则无需实现本方法
			// open(index) {
			// 	// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
			// 	// 原本为'false'，再次设置为'false'会无效
			// 	this.list[index].show = true;
			// 	this.list.map((val, idx) => {
			// 		if (index != idx) this.list[idx].show = false;
			// 	})
			// },
			clickemployee(item) {
				uni.setStorageSync('employeeId',item.id);
				uni.navigateTo({
					url: '../employeedetail/employeedetail'
				})
			}
		}
	};
</script>

<style lang="scss" scoped>
	.input {
		width: 20px;
		margin-left: 30px;
	}

	.input1 {
		width: 20px;
		margin-left: 17px;
	}

	.input2 {
		margin-right: 10px;
	}
	
	.content {
		background-color: #9EC2EC;
	}

	.item {
		display: flex;
		padding: 20rpx;
	}

	image {
		width: 120rpx;
		flex: 0 0 120rpx;
		height: 120rpx;
		margin-right: 20rpx;
		border-radius: 12rpx;
	}

	.title {
		text-align: left;
		font-size: 28rpx;
		color: $u-content-color;
		margin-top: 20rpx;
	}

	.name {
		text-align: left;
		font-size: 20px;
		color: #000000;
		font-weight: 700;
		text-shadow: 1px 1px #778899;
	}

	.search {
		height: 40px;
		width: 40px;
		margin-left: 85%;
	}

	.vertical {
		display: flex;
		flex-direction: column;
	}

	.line {
		display: flex;
		flex-direction: row;
	}

	.fontgap {
		font-size: 20px;
		color: #000000;
		font-weight: 700;
		text-shadow: 1px 1px #778899;
		position: absolute;
		margin-left: 180px;
	}
</style>
