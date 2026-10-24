// Made with Blockbench 5.2.2
// Exported for Minecraft version 1.17 or later with Mojang mappings
// Paste this class into your mod and generate all required imports


public class CustomModel<T extends Entity> extends EntityModel<T> {
	// This layer location should be baked with EntityRendererProvider.Context in the entity renderer and passed into this model's constructor
	public static final ModelLayerLocation LAYER_LOCATION = new ModelLayerLocation(new ResourceLocation("modid", "custommodel"), "main");
	private final ModelPart bb_main;

	public CustomModel(ModelPart root) {
		this.bb_main = root.getChild("bb_main");
	}

	public static LayerDefinition createBodyLayer() {
		MeshDefinition meshdefinition = new MeshDefinition();
		PartDefinition partdefinition = meshdefinition.getRoot();

		PartDefinition bb_main = partdefinition.addOrReplaceChild("bb_main", CubeListBuilder.create().texOffs(-26, -13).addBox(-29.0F, -19.0F, -7.0F, 33.0F, 8.0F, 8.0F, new CubeDeformation(0.0F))
		.texOffs(-44, -13).addBox(-11.0F, -25.0F, -7.0F, 15.0F, 6.0F, 15.0F, new CubeDeformation(0.0F))
		.texOffs(-20, -13).addBox(3.0F, -24.0F, -4.0F, 8.0F, 8.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(-44, -13).addBox(-29.0F, -20.0F, -7.0F, 18.0F, 2.0F, 15.0F, new CubeDeformation(0.0F))
		.texOffs(-44, -13).addBox(-17.0F, -24.0F, -7.0F, 6.0F, 4.0F, 15.0F, new CubeDeformation(0.0F))
		.texOffs(-44, -13).addBox(-29.0F, -24.0F, -7.0F, 12.0F, 4.0F, 15.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -2).addBox(-5.0F, -22.0F, 7.0F, 6.0F, 7.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(-26, -13).addBox(-29.0F, -19.0F, 1.0F, 33.0F, 8.0F, 7.0F, new CubeDeformation(0.0F))
		.texOffs(-28, -8).addBox(1.0F, -18.0F, -4.0F, 22.0F, 4.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(21.0F, -20.0F, -4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(-21, -7).addBox(7.0F, -19.0F, -4.0F, 16.0F, 1.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(-18, -8).addBox(8.0F, -18.0F, -4.0F, 12.0F, 4.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(-28, -8).addBox(-13.0F, -27.0F, -4.0F, 22.0F, 5.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(-19, -8).addBox(10.0F, -28.0F, -4.0F, 13.0F, 4.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(-18, -7).addBox(10.0F, -24.0F, -4.0F, 13.0F, 1.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(17.0F, -20.0F, 4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(17.0F, -19.0F, -4.0F, 2.0F, -1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(12.0F, -20.0F, -4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(13.0F, -20.0F, 4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(21.0F, -20.0F, 4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(21.0F, -23.0F, 4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(17.0F, -23.0F, 4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(13.0F, -23.0F, 4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(21.0F, -23.0F, -4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(17.0F, -22.0F, -4.0F, 2.0F, -1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(1, 1).addBox(12.0F, -23.0F, -4.0F, 2.0F, 1.0F, 1.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -3).addBox(-24.0F, -8.0F, -12.0F, 8.0F, 6.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(-10, -4).addBox(-25.0F, -14.0F, -13.0F, 11.0F, 8.0F, 6.0F, new CubeDeformation(0.0F))
		.texOffs(-10, -4).addBox(-25.0F, -14.0F, 6.0F, 11.0F, 8.0F, 6.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -3).addBox(-24.0F, -5.0F, 6.0F, 8.0F, 6.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -3).addBox(-24.0F, 0.0F, 6.0F, 13.0F, 4.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -3).addBox(-24.0F, 0.0F, -12.0F, 13.0F, 4.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -3).addBox(-24.0F, -8.0F, 6.0F, 8.0F, 6.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -3).addBox(-24.0F, -5.0F, -12.0F, 8.0F, 6.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(-36, -8).addBox(-48.0F, -22.0F, -4.0F, 30.0F, 9.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(-49, -4).addBox(-74.0F, -17.0F, -2.0F, 47.0F, 6.0F, 5.0F, new CubeDeformation(0.0F))
		.texOffs(-15, -9).addBox(5.0F, -27.0F, -5.0F, 7.0F, 10.0F, 11.0F, new CubeDeformation(0.0F))
		.texOffs(-5, 0).addBox(-2.0F, -18.0F, 11.0F, 5.0F, 6.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(-19, -8).addBox(4.0F, -31.0F, -4.0F, 13.0F, 4.0F, 9.0F, new CubeDeformation(0.0F))
		.texOffs(-2, 0).addBox(2.0F, -14.0F, -10.0F, 2.0F, 6.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(-2, 0).addBox(2.0F, -14.0F, 10.0F, 2.0F, 6.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(-5, 0).addBox(-2.0F, -18.0F, -11.0F, 5.0F, 6.0F, 2.0F, new CubeDeformation(0.0F))
		.texOffs(-8, -2).addBox(-5.0F, -22.0F, -10.0F, 6.0F, 7.0F, 4.0F, new CubeDeformation(0.0F))
		.texOffs(-9, -9).addBox(10.0F, -28.0F, -5.0F, 2.0F, 2.0F, 11.0F, new CubeDeformation(0.0F)), PartPose.offset(0.0F, 24.0F, 0.0F));

		return LayerDefinition.create(meshdefinition, 16, 16);
	}

	@Override
	public void setupAnim(Entity entity, float limbSwing, float limbSwingAmount, float ageInTicks, float netHeadYaw, float headPitch) {

	}

	@Override
	public void renderToBuffer(PoseStack poseStack, VertexConsumer vertexConsumer, int packedLight, int packedOverlay, float red, float green, float blue, float alpha) {
		bb_main.render(poseStack, vertexConsumer, packedLight, packedOverlay, red, green, blue, alpha);
	}
}